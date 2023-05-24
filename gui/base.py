from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter


class Shape:
    def __init__(self, pos_x, pos_y, width, height) -> None:
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.heigit = height

        self.rect = QRect(pos_x, pos_y, width, height)

        self.repaint = False

    def draw(self, painter: QPainter) -> None:
        pass

    def update(self):
        self.repaint = True