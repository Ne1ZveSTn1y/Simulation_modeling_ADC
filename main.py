import sys
from gui import SimulationModel
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimulationModel()
    window.show()

    sys.exit(app.exec())