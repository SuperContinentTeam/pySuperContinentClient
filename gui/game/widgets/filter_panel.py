from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect

from utils.size import WORLD_TOP, FILTER_HEIGHT, FILTER_WIDTH, FILTER_LEFT
from utils.colors import BLACK, WHITE
from utils.reference import FLAG_ALIGN_CENTER


class FilterItemPanel:
    def __init__(self, name):
        self.name = name

    def draw(self, painter: QPainter, start_x: int, width: int):
        rect = QRect(start_x, WORLD_TOP, width, FILTER_HEIGHT)
        painter.drawRect(rect)
        painter.drawText(rect, FLAG_ALIGN_CENTER, self.name)


class FilterPanel:
    items = ("探索滤镜", "领土滤镜")

    def __init__(self):
        self.filters = tuple(FilterItemPanel(i) for i in self.items)
        self.item_width = FILTER_WIDTH // len(self.items)
    
    def draw(self, painter: QPainter):
        painter.setPen(BLACK)
        painter.setBrush(WHITE)
        
        for i, f in enumerate(self.filters):
            f.draw(painter, self.item_width * i + FILTER_LEFT, self.item_width)
