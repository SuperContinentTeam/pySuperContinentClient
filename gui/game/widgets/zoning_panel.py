from typing import Optional

from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QPainter

from gui.game.game_state.elements import Block, ZoningBlock
from gui.game.game_state.state import GameState
from utils.colors import BLACK, WHITE
from utils.size import ZONING_HEIGHT, ZONING_LEFT, ZONING_TOP


class ZoningPanel:
    state = GameState()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.display_block: Optional[Block] = None
        self.item_width = ZONING_HEIGHT

    def draw(self, painter: QPainter) -> None:
        painter.setPen(BLACK)
        painter.setBrush(WHITE)

        zoning: Optional[ZoningBlock] = self.state.zoning_map.get(self.display_block)
        if zoning is None:
            painter.drawRect(
                ZONING_LEFT,
                ZONING_TOP,
                ZONING_HEIGHT,
                ZONING_HEIGHT
            )
        else:
            self.item_width = ZONING_HEIGHT // self.display_block.zoning_number
            for zoning in self.state.zoning_map[self.display_block].values():
                rect = QRect(
                    zoning.ix * self.item_width + ZONING_LEFT,
                    zoning.iy * self.item_width + ZONING_TOP,
                    self.item_width,
                    self.item_width
                )
                painter.drawRect(rect)

    def click(self, x, y, button) -> None:
        click = "Left" if button == Qt.MouseButton.LeftButton else "Right"
        if self.display_block is None:
            print(f"{click} in Zoning Area")
        else:
            col = x // self.item_width
            row = y // self.item_width
            k = self.display_block.ix, self.display_block.iy, col, row
            print(f"{click} Click pos: {k}")
