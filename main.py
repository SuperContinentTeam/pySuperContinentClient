import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor
# from gui.start_window import StartWindow
from gui.game.main_panel import MainGamePanel
from gui.single_setting_window import SingleSettingWindow
from gui.start_window import StartWindow


def start_gui():
    app = QApplication(sys.argv)
    # arguments = {
    #     'activeAiModel': False,
    #     'aiCount': 0,
    #     'aiModelPath': '',
    #     'empireColor': QColor(255, 0, 0),
    #     'empireName': '',
    #     'resourceRatio': 1,
    #     'worldSize': 10
    # }
    w = StartWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start_gui()
