from typing import Dict, Tuple

from PyQt5.QtCore import QRect, Qt, pyqtSignal, QObject
from PyQt5.QtGui import QPainter

from gui.game.game_state.block import Block
from utils.colors import BLACK, WHITE
from utils.reference import FLAG_ALIGN_CENTER
from utils.size import WORLD_HEIGHT, WORLD_TOP, GAME_LEFT, GAME_BOTTOM


def check_in(x, y):
    b1 = GAME_LEFT < x < GAME_LEFT + WORLD_HEIGHT
    b2 = WORLD_TOP < y < GAME_BOTTOM
    return b1 and b2


class WorldSignal(QObject):
    update_zoning_panel = pyqtSignal(tuple)


class WorldPanel:
    signal = WorldSignal()

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
            painter.setBrush(WHITE)
            rect = QRect(
                block.ix * self.block_width + GAME_LEFT,
                block.iy * self.block_width + WORLD_TOP,
                self.block_width,
                self.block_width
            )
            painter.drawRect(rect)
            painter.drawText(rect, FLAG_ALIGN_CENTER, f"{block.ix}, {block.iy}")

    def click(self, x, y, button: Qt.MouseButton):
        if not check_in(x, y):
            return

        click = "Left" if button == Qt.LeftButton else "Right"
        col = (x - GAME_LEFT) // self.block_width
        row = (y - WORLD_TOP) // self.block_width

        # 点击地块时 触发更新信号让界面局部刷新区划板块
        self.signal.update_zoning_panel.emit((col, row))  # type: ignore

        print(f"{click} click in Pos({x}, {y}), BlockWidth: {self.block_width}")
