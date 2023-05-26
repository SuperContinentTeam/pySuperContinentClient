import random
from typing import Dict, Tuple

from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect, Qt

from utils.size import WORLD_HEIGHT, WORLD_TOP, GAME_LEFT, GAME_BOTTOM
from utils.colors import BLACK, WHITE
from utils.reference import FLAG_ALIGN_CENTER


class Block:
    def __init__(self, c, r):
        self.ix = c
        self.iy = r
        self.zoning_number = random.randint(3, 6)

    def draw(self, painter: QPainter, width: int):
        painter.setBrush(WHITE)
        rect = QRect(self.ix * width + GAME_LEFT, self.iy * width + WORLD_TOP,  width, width)
        painter.drawRect(rect)
        painter.drawText(rect, FLAG_ALIGN_CENTER, f"{self.ix}, {self.iy}")

    def __str__(self) -> str:
        return f"<Block: {self.ix}, {self.iy}>"


def check_in(x, y):
    b1 = GAME_LEFT < x < GAME_LEFT + WORLD_HEIGHT
    b2 = WORLD_TOP < y < GAME_BOTTOM
    return b1 and b2


class WorldPanel:
    def __init__(self, parent, size=10):
        self.parent = parent
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

    def click(self, x, y, button: Qt.MouseButton):
        if not check_in(x, y):
            return

        click = "Left" if button == Qt.LeftButton else "Right"
        col = (x - GAME_LEFT) // self.block_width
        row = (y - WORLD_TOP) // self.block_width
        block = self.blocks[(col, row)]

        # 点击地块时 触发更新信号让界面局部刷新区划板块
        self.parent.display_block = block
        self.parent.update()

        print(f"{click} click in {block}. Pos({x}, {y}), BlockWidth: {self.block_width}")
