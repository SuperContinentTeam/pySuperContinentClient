from typing import Optional

from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QPainter

from gui.game.game_state.block import Block
from utils.colors import BLACK, WHITE
from utils.reference import FLAG_ALIGN_CENTER
from utils.size import ZONING_HEIGHT, ZONING_LEFT, ZONING_TOP


class ZoningBlock:
    def __init__(self, col, row, block: Block):
        self.ix = col
        self.iy = row
        self.block = block

    def __str__(self):
        return f"<Zoning: {self.ix}, {self.iy}>"


class ZoningPanel:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.display_block: Optional[Block] = None
        self.item_width = ZONING_HEIGHT

    def draw(self, painter: QPainter) -> None:
        painter.setPen(BLACK)
        painter.setBrush(WHITE)

        if self.display_block is None:
            painter.drawRect(
                ZONING_LEFT,
                ZONING_TOP,
                ZONING_HEIGHT,
                ZONING_HEIGHT
            )
        else:
            self.item_width = ZONING_HEIGHT // self.display_block.zoning_number
            for i in range(self.display_block.zoning_number):
                for j in range(self.display_block.zoning_number):
                    rect = QRect(
                        i * self.item_width + ZONING_LEFT,
                        j * self.item_width + ZONING_TOP,
                        self.item_width,
                        self.item_width
                    )
                    painter.drawRect(rect)
                    painter.drawText(rect, FLAG_ALIGN_CENTER, f"{i},{j}")

    def click(self, x, y, button) -> None:
        click = "Left" if button == Qt.MouseButton.LeftButton else "Right"
        if self.display_block is None:
            print(f"{click} in Zoning Area")
        else:
            col = x // self.item_width
            row = y // self.item_width
            k = self.display_block.ix, self.display_block.iy, col, row
            print(f"{click} Click pos: {k}")
