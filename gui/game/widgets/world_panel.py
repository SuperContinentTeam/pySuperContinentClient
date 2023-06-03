from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QPainter, QColor

from gui.game.game_state.elements import Block
from gui.game.game_state.reference import FilterName
from gui.game.game_state.state import GameState
from utils.colors import BLACK, EnvironmentColor, WHITE
from utils.size import WORLD_HEIGHT, WORLD_TOP


def get_current_color(state: GameState, block: Block):
    # 如果是探索滤镜
    if state.filter == FilterName.DISCOVER:
        return EnvironmentColor[block.env] if block.visitable else WHITE

    # 如果是领土滤镜
    if state.filter == FilterName.PLAYER:
        return WHITE if block.player is None else block.player.color

    return WHITE


class WorldPanel:
    state = GameState()

    def __init__(self):
        self.size = self.state.world_size
        self.number = self.size * self.size
        self.block_width = WORLD_HEIGHT // self.size

    def draw(self, painter: QPainter):
        painter.setPen(BLACK)
        for block in self.state.world_map.values():
            painter.setBrush(get_current_color(self.state, block))
            rect = QRect(
                block.ix * self.block_width,
                block.iy * self.block_width + WORLD_TOP,
                self.block_width,
                self.block_width
            )
            painter.drawRect(rect)

    def click(self, x, y, button: Qt.MouseButton):
        click = "Left" if button == Qt.MouseButton.LeftButton else "Right"
        col = x // self.block_width
        row = y // self.block_width

        # 点击地块时 触发更新信号让界面局部刷新区划板块
        self.state.signals.click_world_block.emit((col, row))

        print(f"{click} click in Pos({x}, {y}), BlockWidth: {self.block_width}")
