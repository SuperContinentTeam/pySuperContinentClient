from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtGui import QPainter, QPaintEvent, QMouseEvent, QGuiApplication
from PyQt6.QtWidgets import QMainWindow

from gui.game.game_state.state import GameState
from gui.game.widgets.filter_panel import FilterPanel
from gui.game.widgets.resource_widget import ResourcePanel
from gui.game.widgets.world_panel import WorldPanel
from gui.game.widgets.zoning_widget import ZoningPanel
from utils.settings import TITLE
from utils.size import (
    WIDTH, HEIGHT, ZONING_LEFT, ZONING_RIGHT, ZONING_TOP, ZONING_BOTTOM, RESOURCE_LEFT, RESOURCE_RIGHT, RESOURCE_TOP,
    RESOURCE_BOTTOM
)


class Signal(QObject):
    signal_update_event = pyqtSignal()


class MainGamePanel(QMainWindow):
    signal = Signal()

    def __init__(self, arguments, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_window = self.parent()
        # 初始参数
        self.arguments = arguments
        self.game_state = GameState(10)

        self.setWindowTitle(TITLE)
        self.resize(WIDTH, HEIGHT)
        self.move_center()

        # 资源板块
        self.resource_panel = ResourcePanel()
        # 消息板块
        # self.message_box = MessageBoxPanel(self)
        # 世界板块
        self.world = WorldPanel()
        # 滤镜板块
        self.filter_panel = FilterPanel()
        # 区划板块
        self.zoning_panel = ZoningPanel()

        self.world.signal.update_zoning_panel.connect(self.update_zoning_panel)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        self.resource_panel.draw(painter)
        self.world.draw(painter)
        self.filter_panel.draw(painter)
        self.zoning_panel.draw(painter)

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        pos = a0.pos()
        button = a0.button()
        x, y = pos.x(), pos.y()

        # 检查资源板块
        if RESOURCE_LEFT < x < RESOURCE_RIGHT and RESOURCE_TOP < y < RESOURCE_BOTTOM:
            self.resource_panel.click(x - RESOURCE_LEFT, button)

        #  检查区划板块
        if ZONING_LEFT < x < ZONING_RIGHT and ZONING_TOP < y < ZONING_BOTTOM:
            self.zoning_panel.click(x - ZONING_LEFT, y - ZONING_TOP, button)

        self.world.click(x, y, button)

    def closeEvent(self, a0) -> None:
        if self.last_window:
            self.last_window.show()  # type: ignore

        return super().closeEvent(a0)

    def move_center(self):
        screen = QGuiApplication.primaryScreen().size()

        x = (screen.width() - WIDTH) // 2
        y = (screen.height() - HEIGHT) // 2

        self.move(x, y)

    # 更新区划板块
    def update_zoning_panel(self, pos):
        self.zoning_panel.display_block = self.world.blocks[pos]
        self.update()
