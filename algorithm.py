from abc import ABC, abstractmethod
from random import randint, random
from typing import List

class Application:
    def __init__(self, app_id: int, need_neurons: int):
        self.id = app_id
        self.generation_time = 0 # время появления
        self.required_neurons_count = need_neurons # требуемой количество нейронов
        self.status = "waiting" # waiting, processing, completed, dropped
        self.neurons_involved_count = 0 # количество занятых нейронов
        self.index_input_neuron = -1
        self.last_layer = -1

        self.required_processing_time = 3 * self.required_neurons_count + 2 # требуемое время обработки

    def __str__(self):
        return (f"{self.id}|{self.status}|{self.required_neurons_count}|{self.neurons_involved_count}|"
                f"{self.generation_time}-{self.generation_time + self.required_processing_time}")

class Neuron:
    def __init__(self):
        self.is_working = True # True - исправен, False - неисправен
        self.remaining_processing_time = 0 # оставшееся время обработки
        self.current_application = None # заявка, которой занят нейрон
        self.current_application_id = -1 # -1 - нейрон свободен
        self.required_neurons_count = 0 # требуемое количество нейронов
        self.neurons_involved_count = 0 # количество задействованных нейронов
        self.processed_applications_count = 0 # количество обработанных заявок
        self.dropped_applications_count = 0 # количество необработанных заявок

    def __str__(self):
        return f"{self.current_application_id}|{self.required_neurons_count}|{self.remaining_processing_time}"

    def designation(self) -> str:
        return f"{self.current_application_id}|{self.required_neurons_count}|{self.remaining_processing_time}"

    def take_app(self, app: Application, row: int):
        self.current_application = app
        self.current_application_id = app.id
        self.required_neurons_count = app.required_neurons_count
        self.remaining_processing_time = app.required_processing_time - row

        app.status = "processing"
        app.neurons_involved_count += 1
        app.last_layer += 1

    def set_liberation(self):
        self.remaining_processing_time = 0
        self.current_application = None
        self.current_application_id = -1  # -1 - нейрон свободен
        self.required_neurons_count = 0
        self.neurons_involved_count = 0

class BaseArchitecture(ABC):
    def __init__(self, row_width: list):
        self.simulation_tact = 0 # такт моделирования
        self.topology: List[List[Neuron]] = [[]] # сама архитектура
        self.row_width_list = row_width # обозначает ширину каждого ряда, с помощью неё можно изменять архитектуру
        self.is_input_stream_enabled = [True for _ in range(self.row_width_list[0])] # включен ли входной поток
        self.time_of_appearance = [[0, 0] for _ in range(self.row_width_list[0])] # (первое появление заявки, период появления заявки)

        self.generate_topology()

    @abstractmethod
    def generate_topology(self):
        pass

    @abstractmethod
    def taking_the_next_layer(self, app: Application, current_layer: int, current_column: int):
        pass

    def print_topology(self):
        for i in range(len(self.topology)):
            res = ""
            for j in range(len(self.topology[i])):
                res += self.topology[i][j].designation() + "\t"
            print(res)

    def check_max_column(self, check_layer: int, check_column: int) -> int:
        if check_column != (len(self.topology[check_layer])):
            return check_column
        return 0

class MatrixArchitecture(BaseArchitecture):
    def generate_topology(self):
        self.topology = [[Neuron() for _ in range(self.row_width_list[0])] for _ in range(len(self.row_width_list))]

    def taking_the_next_layer(self, app: Application, current_layer: int, current_column: int) -> bool:
        if (app.neurons_involved_count == app.required_neurons_count) or (app.last_layer != current_layer):
            return True

        increment_column = self.check_max_column(current_layer, current_column + 1)

        if ((self.topology[current_layer + 1][current_column].current_application is None) and
                self.topology[current_layer + 1][current_column].is_working):
            self.topology[current_layer + 1][current_column].take_app(app, current_layer + 1)
            return True
        elif ((self.topology[current_layer + 1][current_column - 1].current_application is None) and
              self.topology[current_layer + 1][current_column - 1].is_working):
            self.topology[current_layer + 1][current_column - 1].take_app(app, current_layer + 1)
            return True
        elif ((self.topology[current_layer + 1][increment_column].current_application is None) and
              self.topology[current_layer + 1][increment_column].is_working):
            self.topology[current_layer + 1][increment_column].take_app(app, current_layer + 1)
            return True
        return False

class SimulationController:
    def __init__(self, architecture: BaseArchitecture, periods: List[List[int]] = None):
        self.current_tick = 0 # текущий такт моделирования
        self.current_architecture = architecture
        self.max_count_app = 15 # максимальное количество генерируемых заявок
        # список максимального количества генерируемых заявок для каждого входного нейрона
        self.list_max_count_app = [self.max_count_app for _ in range(self.current_architecture.row_width_list[0])]
        # список количества сгенерированных уже заявок для каждого входного нейрона
        self.list_count_app = [0 for _ in range(self.current_architecture.row_width_list[0])]

        self.flag_rnd_breakdowns = False
        self.probability_of_neuron_failure: float = 0.01
        self.res_rnd_breakdowns: List[List[int]] = []

        if periods is None:
            # [первый такт появления, период появления]
            self.time_of_appearance = [[i + 1, 20] for i in range(self.current_architecture.row_width_list[0])]
        else:
            self.time_of_appearance = periods

        self.applications_in_process = []  # сейчас обрабатываемые заявки
        self.applications_completed = [[] for _ in range(self.current_architecture.row_width_list[0])]  # обработанные заявки
        self.applications_dropped = [[] for _ in range(self.current_architecture.row_width_list[0])]  # заявки, получившие отказ
        self.applications_count = 0  # общее количество заявок

    def output_of_information(self) -> list:
        info_input_neuron = []
        sum_dropped_application = 0
        for i in range(self.current_architecture.row_width_list[0]):
            sum_dropped_application += self.current_architecture.topology[0][i].dropped_applications_count
            try:
                info_input_neuron.append(round(self.current_architecture.topology[0][i].dropped_applications_count /
                                         (self.current_architecture.topology[0][i].processed_applications_count +
                                         self.current_architecture.topology[0][i].dropped_applications_count), 4))
            except ZeroDivisionError:
                info_input_neuron.append(0)
        return [self.applications_count, round(sum_dropped_application / self.applications_count, 4), info_input_neuron]

    def next_tick(self):
        # self.res_rnd_breakdowns.clear()
        self.current_tick += 1
        # if self.flag_rnd_breakdowns:
        #     self.res_rnd_breakdowns = self.rnd_breakdowns()
        for i in self.current_architecture.topology:
            for j in range(len(i)):
                if i[j].remaining_processing_time > 0:
                    i[j].remaining_processing_time -= 1
        self.search_for_an_application()
        self.check_release_application()
        self.check_and_generate_applications()

    def auto_mode(self):
        while True:
            self.rnd_breakdowns(True)
            # print(self.res_rnd_breakdowns)
            self.next_tick()
            if self.check_off_mode_auto():
                break
        print("Completed! Mode auto -> off")

    def check_off_mode_auto(self) -> bool:
        for i in range(len(self.current_architecture.topology[0])):
            if (self.list_count_app[i] != self.list_max_count_app[i]) and self.current_architecture.topology[0][i].is_working:
                return False

        for i in range(len(self.current_architecture.topology)):
            for j in range(len(self.current_architecture.topology[i])):
                if self.current_architecture.topology[i][j].remaining_processing_time != 0:
                    return False
        return True

    def jerk(self, input_tick: int):
        self.res_rnd_breakdowns.clear()
        for _ in range(input_tick):
            self.rnd_breakdowns(True)
            self.next_tick()

    def check_and_generate_applications(self):
        for i in range(len(self.time_of_appearance)):
            if self.list_count_app[i] != self.list_max_count_app[i]:
                if (((self.time_of_appearance[i][0] == self.current_tick) or
                        ((self.current_tick - self.time_of_appearance[i][0]) % self.time_of_appearance[i][1] == 0)) and
                        self.current_architecture.topology[0][i].is_working):
                    app = self.generate_applications()
                    app.index_input_neuron = i
                    self.applications_in_process.append(app)
                    self.current_architecture.topology[0][i].take_app(app, 0)
                    self.list_count_app[i] += 1

    def generate_applications(self) -> Application:
        self.applications_count += 1
        return Application(self.applications_count, randint(2, 6))

    def search_for_an_application(self):
        for i in range(len(self.current_architecture.topology) - 1, -1, -1):
            for j in range(len(self.current_architecture.topology[i])):
                if self.current_architecture.topology[i][j].current_application is not None:
                     if not(self.current_architecture.taking_the_next_layer(self.current_architecture.topology[i][j].current_application, i, j)):
                         self.dropped_application(self.current_architecture.topology[i][j].current_application)

    def check_release_application(self):
        for i in range(len(self.current_architecture.topology[0])):
            if ((self.current_architecture.topology[0][i].current_application is not None) and
                    (self.current_architecture.topology[0][i].remaining_processing_time == 0)):
                self.release_application(self.current_architecture.topology[0][i].current_application)

    def release_application(self, app: Application):
        app.status = "completed"
        self.applications_completed[app.index_input_neuron].append(app)
        self.applications_in_process.remove(app)
        for i in self.current_architecture.topology:
            for j in range(len(i)):
                if i[j].current_application == app:
                    i[j].set_liberation()
                    i[j].processed_applications_count += 1

    def dropped_application(self, app):
        app.status = "dropped"
        self.applications_dropped[app.index_input_neuron].append(app)
        self.applications_in_process.remove(app)
        for i in self.current_architecture.topology:
            for j in range(len(i)):
                if i[j].current_application == app:
                    i[j].set_liberation()
                    i[j].dropped_applications_count += 1

    def rnd_breakdowns(self, flag: bool = False) -> list:
        res = []
        for r in range(len(self.current_architecture.row_width_list)):
            for c in range(self.current_architecture.row_width_list[r]):
                if (random() <= self.probability_of_neuron_failure) and self.current_architecture.topology[r][c].is_working:
                    if flag:
                        self.current_architecture.topology[r][c].is_working = False
                        self.res_rnd_breakdowns.append([self.current_tick, r, c])
                    res.append([self.current_tick, r, c])
        return res




if __name__ == "__main__":
    matr = MatrixArchitecture([3, 3, 3, 3, 3, 3])
    matr.print_topology()

    controller = SimulationController(matr)
    print(controller.current_tick)
    controller.next_tick()
    print(controller.current_tick)
    matr.print_topology()
    print(controller.current_tick)
    matr.print_topology()
    controller.next_tick()
    print(controller.current_tick)
    matr.print_topology()
    controller.next_tick()
    print(controller.current_tick)
    matr.print_topology()
    controller.next_tick()
    print(controller.current_tick)
    matr.print_topology()