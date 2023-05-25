from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect

from utils.size import WORLD_TOP, FLITER_HEIGHT, FLITER_WIDTH, FLITER_LEFT
from utils.colors import BLACK, WHITE
from utils.reference import FLAG_ALIGN_CENTER


class FliterItemPanel:
    def __init__(self, name):
        self.name = name

    def draw(self, painter: QPainter, start_x: int, width: int):
        rect = QRect(start_x, WORLD_TOP, width, FLITER_HEIGHT)
        painter.drawRect(rect)
        painter.drawText(rect, FLAG_ALIGN_CENTER, self.name)


class FliterPanel:
    items = ("探索滤镜", "领土滤镜")

    def __init__(self):
        self.fliters = tuple(FliterItemPanel(i) for i in self.items)
        self.item_width = FLITER_WIDTH // len(self.items)
    
    def draw(self, painter: QPainter):
        painter.setPen(BLACK)
        painter.setBrush(WHITE)
        
        for i, fliter in enumerate(self.fliters):
            fliter.draw(painter, self.item_width * i + FLITER_LEFT, self.item_width)
