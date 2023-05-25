from typing import Dict, Tuple

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect, Qt

from utils.size import ZONING_LEFT, ZONING_TOP, ZONING_HEIGHT
from utils.colors import BLACK, WHITE
from utils.reference import FLAG_ALIGN_CENTER

from gui.game.widgets.world_panel import Block


class ZoningBlock:
    def __init__(self, c, r, block: Block):
        self.ix = c
        self.iy = r
        self.block = block

    def __str__(self) -> str:
        return f"<Zoning: {self.ix}, {self.iy}>"

    def draw(self, painter: QPainter, width: int):
        print(self)
        painter.setBrush(WHITE)
        rect = QRect(
            self.ix * width + ZONING_LEFT,
            self.iy * width + ZONING_TOP,
            width,
            width
        )
        painter.drawRect(rect)
        painter.drawText(rect, FLAG_ALIGN_CENTER, f"{self.ix}, {self.iy}")


class ZoningPanel:
    def __init__(self, size=3):
        self.size = 3
        self.number = size * size
        self.zoning_width = ZONING_HEIGHT // size

        temp_b = Block(0, 0)
        self.zonings: Dict[Tuple[int, int], ZoningBlock] = {
            (i, j): ZoningBlock(i, j, temp_b)
            for i in range(size) for j in range(size)
        }

    def draw(self, painter: QPainter):
        painter.setPen(BLACK)
        for zoning in self.zonings.values():
            zoning.draw(painter, self.zoning_width)
