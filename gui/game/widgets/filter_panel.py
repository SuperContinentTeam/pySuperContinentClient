from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QPainter

from utils.colors import BLACK, WHITE
from utils.reference import FLAG_ALIGN_CENTER
from utils.size import WORLD_TOP, FILTER_HEIGHT, FILTER_WIDTH, FILTER_LEFT


def check_in(x, y):
    b1 = FILTER_LEFT < x < FILTER_LEFT + FILTER_WIDTH
    b2 = WORLD_TOP < y < WORLD_TOP + FILTER_HEIGHT
    return b1 and b2


class FilterItemPanel:
    def __init__(self, name):
        self.name = name


class FilterPanel:
    items = ("探索滤镜", "领土滤镜")

    def __init__(self):
        self.filters = tuple(FilterItemPanel(i) for i in self.items)
        self.item_width = FILTER_WIDTH // len(self.items)

    def click(self, x, button: Qt.MouseButton):
        f: FilterItemPanel = self.filters[x // self.item_width]
        click = "Left" if button == Qt.MouseButton.LeftButton else "Right"
        print(f"{click} click in: {f.name}")

    def draw(self, painter: QPainter):
        painter.setPen(BLACK)
        painter.setBrush(WHITE)

        for i, f in enumerate(self.filters):
            rect = QRect(self.item_width * i + FILTER_LEFT, WORLD_TOP, self.item_width, FILTER_HEIGHT)
            painter.drawRect(rect)
            painter.drawText(rect, FLAG_ALIGN_CENTER, f.name)
