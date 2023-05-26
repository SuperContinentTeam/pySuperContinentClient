from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QPainter, QPaintEvent, QMouseEvent
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from gui.game.widgets.filter_panel import FilterPanel
from gui.game.widgets.resource_widget import ResourceWidget
from gui.game.widgets.world_panel import WorldPanel
from gui.game.widgets.zoning_panel import ZoningPanel
from utils.settings import TITLE
from utils.size import WIDTH, HEIGHT


class Signal(QObject):
    signal_update_event = pyqtSignal()


class MainGamePanel(QMainWindow):
    signal = Signal()

    def __init__(self, arguments, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_window = self.parent()
        # 初始参数
        self.arguments = arguments
        # self.game_state = GameState(10)

        self.setWindowTitle(TITLE)
        self.resize(WIDTH, HEIGHT)
        self.center()

        # 资源板块
        self.resource_widget = ResourceWidget(self)
        # 消息板块
        # self.message_box = MessageBoxPanel(self)
        # 世界板块
        self.world = WorldPanel()
        self.world.signal.update_zoning_panel.connect(self.update_zoning_panel)
        # 滤镜板块
        self.filter_panel = FilterPanel()
        # 区划板块
        self.zoning_panel = ZoningPanel(self.world.blocks.values())
        # 被显示区划的世界地块
        self.display_block = None

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        # self.resource_panel.draw(painter)
        self.world.draw(painter)
        self.filter_panel.draw(painter)
        self.zoning_panel.draw(painter, self.display_block)

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        pos = a0.pos()
        button = a0.button()
        x, y = pos.x(), pos.y()

        # self.resource_panel.click(x, y, button)
        self.world.click(x, y, button)

    def closeEvent(self, a0) -> None:
        if self.last_window:
            self.last_window.show()  # type: ignore

        return super().closeEvent(a0)

    def center(self):
        screen = QDesktopWidget().screenGeometry()

        x = (screen.width() - WIDTH) // 2
        y = (screen.height() - HEIGHT) // 2

        self.move(x, y)

    # 更新区划板块
    def update_zoning_panel(self, pos):
        self.display_block = self.world.blocks[pos]
        self.update()
