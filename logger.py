import logging
import os
from time import strftime

class SimulationLogger:
    """Класс для логирования неисправностей нейронов в формате CSV.
    Обеспечивает создание файла, запись заголовков и структурированное
    добавление данных о состоянии ячеек (строка/колонка) на каждом такте.
    """

    def __init__(self, folder_name: str = "Experiments result", filename: str = f"simulation_results_{strftime("%d%m%Y%H%M%S")}.csv"):
        """Инициализирует объект логгера и подготавливает файл для записи.

        :param folder_name: Путь к файлу
        :param filename: Имя CSV-файла с результатами.
        """

        self.folder_name = folder_name
        # Если нет такой папки, то создаём
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

        self.filename = os.path.join(self.folder_name, filename)

        # Очищаем старый файл и записываем заголовки столбцов при создании объекта
        self.__prepare_csv_file()

        # Настраиваем конфигурацию встроенного модуля logging
        self.__configure_logging()

    def __prepare_csv_file(self):

        # Создает или перезаписывает файл, добавляя в него строку заголовков.

        with open(self.filename, "w", encoding="utf-8") as f:
            # Заголовки разделены точкой с запятой для корректного импорта в Excel/PostgreSQL
            f.write("current_tick;row;column;result\n")

    def __configure_logging(self):

        # Задает формат строки и режим добавления данных.

        # Настраиваем базовый логгер.
        # %(tick)d, %(row)d, %(col)d, %(res)s — кастомные переменные,
        # которые мы будем передавать при каждом событии.
        logging.basicConfig(
            filename=self.filename,
            filemode="a",  # Режим 'a' (append) позволяет дописывать данные, не стирая заголовок
            level=logging.INFO,
            format="%(tick)d;%(row)d;%(col)d;%(res)s",
        )

    def log_status(self, tick: int, row: int, column: int, is_working: bool):
        """Публичный интерфейс класса для фиксации состояния объекта моделирования.

        :param tick: Текущий такт моделирования (current_tick)
        :param row: Индекс строки матрицы/сетки (row)
        :param column: Индекс колонки матрицы/сетки (column)
        :param is_working: Статус элемента. True -> 'working', False -> 'break' (результат после нажатия)
        """
        # Преобразуем логический флаг в нужные текстовые маркеры (break/working)
        status_text = "working" if not(is_working) else "break"

        # Передаем параметры через словарь 'extra'.
        # Ключи словаря должны строго совпадать со спецификаторами в свойстве format выше.
        logging.info(
            "",  # Само сообщение оставляем пустым, так как вся структура задана в формате
            extra={"tick": tick, "row": row, "col": column, "res": status_text},
        )

if __name__ == "__main__":
    import random

    print("Инициализация логгера симуляции...")
    # Создаем экземпляр нашего класса логгера
    sim_logger = SimulationLogger()

    print("Запуск имитации тактов симуляции...")

    # Имитируем сетку 3х3 в течение 5 тактов моделирования
    for current_tick in range(1, 6):
        for r in range(3):
            for c in range(3):

                # Случайным образом симулируем поломку элемента (с шансом 15%)
                element_health = random.random() < 0.15

                # Вызываем метод объекта для записи текущего состояния ячейки
                sim_logger.log_status(
                    tick=current_tick, row=r, column=c, is_working=element_health
                )

    print(
        f"Моделирование завершено. Файл '{sim_logger.filename}' успешно обновлен."
    )
