import sys
import algorithm
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
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

        # Генерация матрицы
        self.generate_matrix(rows=self.rows, cols=self.cols)
        self.current_architecture = algorithm.MatrixArchitecture(row_width=self.row_width)
        self.sController = algorithm.SimulationController(self.current_architecture)

        # Привязка действий к кнопкам
        self.ui.btn_next_tick.clicked.connect(self.click_next_tick)

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
                btn.setStyleSheet(u"color: #000000;\n"
                                  "background-color: #FFFFFF;\n"
                                  "font-size: 15px;\n"
                                  "border: 1px solid rgba(0, 0, 0, 0.4);\n"
                                  "border-radius: 5px;")

                btn.move(x_coordinate, y_coordinate)

                btn.setCheckable(True)
                btn.clicked.connect(lambda checked, row=r, col=c, current_btn=btn: self.on_matrix_click(checked, row, col, current_btn))

                btn.show()

                self.btn_neurons_list[r].append(btn)

                c_res = c + 1
            self.row_width.append(c_res)
        print(self.row_width)

    def on_matrix_click(self, checked: bool, row: int, col: int, current_btn: QPushButton):
        print(f"Нажата кнопка: строка {row}, столбец {col}")
        self.ui.result_output.append(f"{checked} Выбрана ячейка [{row}, {col}]")

        if checked:
            current_btn.setStyleSheet(u"color: #000000;\n"
                                      "background-color: #FF0000;\n"
                                      "font-size: 15px;\n"
                                      "border: 1px solid rgba(0, 0, 0, 0.4);\n"
                                      "border-radius: 5px;")
        else:
            current_btn.setStyleSheet(u"color: #000000;\n"
                                  "background-color: #FFFFFF;\n"
                                  "font-size: 15px;\n"
                                  "border: 1px solid rgba(0, 0, 0, 0.4);\n"
                                  "border-radius: 5px;")

    def click_next_tick(self):
        self.sController.next_tick()
        self.ui.label_current_tick.setText(f"Current tick: {self.sController.current_tick}")
        self.update_name_btn()

    def update_name_btn(self):
        for r in range(len(self.btn_neurons_list)):
            for c in range(len(self.btn_neurons_list[r])):
                self.btn_neurons_list[r][c].setText(self.current_architecture.topology[r][c].designation())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimulationModel()
    window.show()

    sys.exit(app.exec())