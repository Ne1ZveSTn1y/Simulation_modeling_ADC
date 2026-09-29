import algorithm
from logger import SimulationLogger
from PySide6.QtWidgets import QMainWindow, QPushButton
from main_window import Ui_MainWindow
from typing import List

class SimulationModel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.row_width = []
        self.rows = 6
        self.cols = 4
        self.btn_neurons_list: List[List[QPushButton]] = [[]]


        # список цветов до 16 (последний цвет для свободных нейронов)
        self.color_list = ["#00FF00", "#00FFFF", "#FFFF00", "#0000FF", "#008000", "#FF1493", "#EE82EE", "#00BFFF",
                           "#00FF7F", "#FFA500", "#F0E68C", "#E6E6FA", "#D2B48C", "#808000", "#FF7F50", "#6A5ACD",
                           "#FFFFFF"]

        # Добавление логгера
        self.sLogger = SimulationLogger()

        # Генерация матрицы
        self.generate_matrix(rows=self.rows, cols=self.cols)
        self.current_architecture = algorithm.MatrixArchitecture(row_width=self.row_width)
        self.sController = algorithm.SimulationController(self.current_architecture)

        self.sController.probability_of_neuron_failure = 0.001

        # Привязка действий к элементам
        self.ui.btn_next_tick.clicked.connect(self.click_next_tick)
        self.ui.btn_auto.clicked.connect(self.click_auto_mode)
        self.ui.btn_jerk.clicked.connect(self.click_jerk)

        self.ui.radio_rnd_break_on.toggled.connect(self.radio_rnd_break_changed)
        self.ui.radio_rnd_break_off.toggled.connect(self.radio_rnd_break_changed)

    def generate_matrix(self, rows: int = 6, cols: int = 4):
        parent_field = self.ui.neurons_container

        # Очищение поля от старых кнопок перед новой генерацией
        for child in parent_field.findChildren(QPushButton):
            child.deleteLater()
        self.btn_neurons_list.clear()
        self.btn_neurons_list = [[] for _ in range(rows)]

        # Настройка размеров и отступов в пикселях
        btn_width = 100
        btn_height = 25
        margin_x = 15
        margin_y = 15
        spacing_x = 8
        spacing_y = 8

        for r in range(rows):
            c_res = 0
            for c in range(cols):
                x_coordinate = margin_x + c * (btn_width + spacing_x)
                y_coordinate = margin_y + r * (btn_height + spacing_y)

                btn = QPushButton(f"{r}, {c}", parent_field)

                btn.setFixedSize(btn_width, btn_height)
                btn.setStyleSheet("color: #000000;\n"
                                  "background-color: #FFFFFF;\n"
                                  "font-size: 15px;\n"
                                  "border: 1px solid rgba(0, 0, 0, 0.4);\n"
                                  "border-radius: 5px;")

                btn.move(x_coordinate, y_coordinate)

                btn.setCheckable(True)
                btn.clicked.connect(lambda checked, row=r, col=c, current_btn=btn: self.on_neuron_click(checked, row, col, current_btn))

                btn.show()

                self.btn_neurons_list[r].append(btn)

                c_res = c + 1
            self.row_width.append(c_res)

    def on_neuron_click(self, checked: bool, row: int, col: int, current_btn: QPushButton):
        self.ui.result_output.append(f"Выбрана ячейка [{row}, {col}]; Такт {self.sController.current_tick}")
        self.current_architecture.topology[row][col].is_working = not checked
        if not self.sController.flag_rnd_breakdowns:
            self.sLogger.log_status(self.sController.current_tick, row, col, checked)

        if checked:
            current_btn.setStyleSheet("color: #000000;\n"
                                      "background-color: #FF0000;\n"
                                      "font-size: 15px;\n"
                                      "border: 1px solid rgba(0, 0, 0, 0.4);\n"
                                      "border-radius: 5px;")
        else:
            current_btn.setStyleSheet("color: #000000;\n"
                                  "background-color: #FFFFFF;\n"
                                  "font-size: 15px;\n"
                                  "border: 1px solid rgba(0, 0, 0, 0.4);\n"
                                  "border-radius: 5px;")

    def click_next_tick(self):
        if self.sController.flag_rnd_breakdowns:
            self.rnd_break(self.sController.rnd_breakdowns(False))
        self.sController.next_tick()
        info = self.sController.output_of_information()
        self.ui.label_current_tick.setText(f"Current tick: {self.sController.current_tick}")
        self.ui.result_output.append(f"Такт: {self.sController.current_tick}: {info[0]}; {info[1]}; {info[2]}")
        self.update_name_btn()

    def click_auto_mode(self):
        self.sController.auto_mode()
        if self.sController.flag_rnd_breakdowns:
            self.rnd_break(self.sController.res_rnd_breakdowns)
        self.ui.label_current_tick.setText(f"Current tick: {self.sController.current_tick}")
        info = self.sController.output_of_information()
        self.ui.result_output.append(f"Конец моделирования: {info[0]}; {info[1]}; {info[2]}")
        self.update_name_btn()

    def click_jerk(self):
        user_input = self.ui.tick_input_number.text().strip()
        try:
            self.sController.jerk(int(user_input))
            if self.sController.flag_rnd_breakdowns:
                self.rnd_break(self.sController.res_rnd_breakdowns)
            self.ui.label_current_tick.setText(f"Current tick: {self.sController.current_tick}")
            self.update_name_btn()
        except ValueError:
            print("Преобразование прошло неудачно")

    def radio_rnd_break_changed(self):
        # print("Тык")
        # self.sController.flag_rnd_breakdowns = not self.sController.flag_rnd_breakdowns

        if self.ui.radio_rnd_break_on.isChecked():
            self.sController.flag_rnd_breakdowns = True
        else:
            self.sController.flag_rnd_breakdowns = False

    def rnd_break(self, list_rnd_breakdowns: List[List[int]]):
        for i in range(len(list_rnd_breakdowns)):
            self.sLogger.log_status(list_rnd_breakdowns[i][0], list_rnd_breakdowns[i][1], list_rnd_breakdowns[i][2], True)
            self.btn_neurons_list[list_rnd_breakdowns[i][1]][list_rnd_breakdowns[i][2]].click()

    def update_name_btn(self):
        for r in range(len(self.btn_neurons_list)):
            for c in range(len(self.btn_neurons_list[r])):
                btn_name = self.current_architecture.topology[r][c].designation()
                self.btn_neurons_list[r][c].setText(btn_name)
                id_app = int(btn_name.split("|")[0])
                id_app = 16 if id_app == -1 else id_app % 16
                self.btn_neurons_list[r][c].setStyleSheet(f"color: #000000;"
                                      f"background-color: {self.color_list[id_app] if not(self.btn_neurons_list[r][c].isChecked()) else "#FF0000"};"
                                      f"font-size: 15px;"
                                      f"border: 1px solid rgba(0, 0, 0, 0.4);"
                                      f"border-radius: 5px;")