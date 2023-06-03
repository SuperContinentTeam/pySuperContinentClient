from typing import Dict, Tuple

from PyQt6.QtCore import QRect, Qt, pyqtSignal, QObject
from PyQt6.QtGui import QPainter

from gui.game.game_state.block import Block
from gui.game.game_state.state import GameState
from utils.colors import BLACK, WHITE
from utils.reference import FLAG_ALIGN_CENTER
from utils.size import WORLD_HEIGHT, WORLD_TOP


class WorldPanel:
    state = GameState()

    def __init__(self):
        self.size = self.state.world_size
        self.number = self.size * self.size
        self.block_width = WORLD_HEIGHT // self.size

    def draw(self, painter: QPainter):
        painter.setPen(BLACK)
        for block in self.state.world_map.values():
            painter.setBrush(WHITE)
            rect = QRect(
                block.ix * self.block_width,
                block.iy * self.block_width + WORLD_TOP,
                self.block_width,
                self.block_width
            )
            painter.drawRect(rect)
            painter.drawText(rect, FLAG_ALIGN_CENTER, f"{block.ix}, {block.iy}")

    def click(self, x, y, button: Qt.MouseButton):
        click = "Left" if button == Qt.MouseButton.LeftButton else "Right"
        col = x // self.block_width
        row = y // self.block_width

        # 点击地块时 触发更新信号让界面局部刷新区划板块
        self.state.signals.click_world_block.emit((col, row))

        print(f"{click} click in Pos({x}, {y}), BlockWidth: {self.block_width}")
