import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor
# from gui.start_window import StartWindow
from gui.game.main_panel import MainGamePanel


def start_gui():
    app = QApplication(sys.argv)
    # start_window = StartWindow()
    arguments = {
        'activeAiModel': False,
        'aiCount': 0,
        'aiModelPath': '',
        'empireColor': QColor(255, 0, 0),
        'empireName': '',
        'resourceRatio': 1,
        'worldSize': 10
    }
    start_window = MainGamePanel(arguments=arguments)
    start_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start_gui()
