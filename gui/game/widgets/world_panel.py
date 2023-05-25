from typing import Dict, Tuple

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect, Qt

from utils.size import WORLD_HEIGHT, WORLD_TOP, GAME_LEFT, GAME_BOTTOM
from utils.colors import BLACK, WHITE


class Block:
    def __init__(self, c, r):
        self.ix = c
        self.iy = r

    def draw(self, painter: QPainter, width: int):
        painter.setBrush(WHITE)
        rect = QRect(self.ix * width + GAME_LEFT, self.iy * width + WORLD_TOP,  width, width)
        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignHCenter | Qt.AlignVCenter, f"{self.ix}, {self.iy}")

    def __str__(self) -> str:
        return f"<Block: {self.ix}, {self.iy}>"

class WorldPanel:
    def __init__(self, size=10):
        self.size = size
        self.number = size * size
        self.block_width = WORLD_HEIGHT // size

        self.blocks: Dict[Tuple[int, int], Block] = {
            (i, j): Block(i, j)
            for i in range(size) for j in range(size)
        }

    def draw(self, painter: QPainter):
        painter.setPen(BLACK)
        for block in self.blocks.values():
            block.draw(painter, self.block_width)

    def check_in(self, x, y):
        b1 = GAME_LEFT < x < GAME_LEFT + WORLD_HEIGHT
        b2 = WORLD_TOP < y < GAME_BOTTOM
        return b1 and b2

    def click(self, x, y, button: Qt.MouseButton):
        if not self.check_in(x, y):
            return

        click = "Left" if button == Qt.LeftButton else "Right"
        col = (x - GAME_LEFT) // self.block_width
        row = (y - WORLD_TOP) // self.block_width
        block = self.blocks[(col, row)]
        print(f"{click} click in {block}. Pos({x}, {y}), BlockWidth: {self.block_width}")
