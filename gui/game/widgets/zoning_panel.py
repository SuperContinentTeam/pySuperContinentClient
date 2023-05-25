from typing import Dict, Tuple, Iterable

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect

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
    rect = QRect(
        ZONING_LEFT,
        ZONING_TOP,
        ZONING_HEIGHT,
        ZONING_HEIGHT
    )

    def __init__(self, blocks: Iterable[Block]):
        self.zonings: Dict[Tuple[int, int, int, int], ZoningBlock] = dict()
        self.init_zonings(blocks)

    def init_zonings(self, blocks: Iterable[Block]):
        for block in blocks:
            for i in range(block.zoning_number):
                for j in range(block.zoning_number):
                    k = block.ix, block.iy, i, j
                    self.zonings[k] = ZoningBlock(i, j, block)

    def draw(self, painter: QPainter, block: Block = None):
        painter.setPen(BLACK)
        if block is None:
            painter.drawRect(self.rect)
        else:
            item_width = ZONING_HEIGHT // block.zoning_number
            for i in range(block.zoning_number):
                for j in range(block.zoning_number):
                    k = block.ix, block.iy, i, j
                    zoning_block = self.zonings[k]
                    zoning_block.draw(painter, item_width)
