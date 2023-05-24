# from PyQt5.QtCore import QTimer
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton
# from PyQt5.QtCore import

from utils.settings import *


class SingleSettingWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle(TITLE)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.parent().show()

        return super().closeEvent(a0)

    #     self.timer = QTimer(self)
    #     self.tick = 1

    #     self.timer.timeout.connect(self.receiver_from_server)
    #     self.timer.start(1000)

    # def receiver_from_server(self):
    #     print("Hello world", self.tick)
    #     self.tick += 1


# 绘制图片
# img = QImage("xxx.png")
# rect = QRect(x, y, img.width()/2, img.height()/2)
# painter.drawImage(rect, img)
