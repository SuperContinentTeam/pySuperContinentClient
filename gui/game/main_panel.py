from PyQt6.QtCore import pyqtSignal, QObject, Qt
from PyQt6.QtGui import QPainter, QPaintEvent, QMouseEvent, QGuiApplication
from PyQt6.QtWidgets import QMainWindow

from gui.game.game_state.reference import FilterName
from gui.game.game_state.state import GameState
from gui.game.websocket_client.client import WSClientThread
from gui.game.widgets.filter_panel import FilterPanel
from gui.game.widgets.information_panel import InformationPanel
from gui.game.widgets.message_panel import MessageBoxPanel
from gui.game.widgets.resource_widget import ResourcePanel
from gui.game.widgets.schedule_panel import SchedulePanel
from gui.game.widgets.text_input_panel import TextInputPanel
from gui.game.widgets.world_panel import WorldPanel
from gui.game.widgets.zoning_panel import ZoningPanel
from utils.settings import TITLE, SERVER
from utils.size import (
    WIDTH, HEIGHT, ZONING_LEFT, ZONING_RIGHT, ZONING_TOP, ZONING_BOTTOM, RESOURCE_LEFT, RESOURCE_RIGHT, RESOURCE_TOP,
    RESOURCE_BOTTOM, WORLD_LEFT, WORLD_RIGHT, WORLD_TOP, WORLD_BOTTOM, FILTER_LEFT, FILTER_RIGHT, FILTER_TOP,
    FILTER_BOTTOM
)


class Signal(QObject):
    signal_update_event = pyqtSignal()


class MainGamePanel(QMainWindow):
    signal = Signal()

    def __init__(self, arguments, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ws_thread = None
        self.last_window = self.parent()
        # 初始参数
        self.arguments = arguments
        self.state = GameState(10)

        self.setWindowTitle(TITLE)
        self.setWindowFlags(
            Qt.WindowType.Window | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowCloseButtonHint
        )
        self.setFixedSize(WIDTH, HEIGHT)
        self.move_center()

        # 资源板块
        self.resource_panel = ResourcePanel()
        # 世界板块
        self.world = WorldPanel()
        # 滤镜板块
        self.filter_panel = FilterPanel()
        # 区划板块
        self.zoning_panel = ZoningPanel()
        # 进度板块
        self.schedule_panel = SchedulePanel(self)
        # 消息板块
        self.message_box = MessageBoxPanel(self)
        # 消息输入框
        self.text_input = TextInputPanel(self)
        # 信息显示框
        self.information_panel = InformationPanel(self)

        # 初始化信号连接
        self.init_signal()
        # 创建ws客户端线程
        self.init_ws()

    def init_ws(self):
        self.ws_thread = WSClientThread(SERVER)
        self.ws_thread.message_received.connect(lambda message: print("Received:", message))
        self.ws_thread.start()

    def init_signal(self):
        s = self.state.signals

        s.click_world_block.connect(self.update_zoning_panel)
        s.click_filter_panel.connect(self.update_world_display)

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

        # 检查世界板块
        if WORLD_LEFT < x < WORLD_RIGHT and WORLD_TOP < y < WORLD_BOTTOM:
            self.world.click(x - WORLD_LEFT, y - WORLD_TOP, button)

        # 检查滤镜板块
        if FILTER_LEFT < x < FILTER_RIGHT and FILTER_TOP < y < FILTER_BOTTOM:
            self.filter_panel.click(x - FILTER_LEFT, button)

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
        self.zoning_panel.display_block = self.state.world_map[pos]
        self.update()

    # 选择滤镜后更新地图渲染
    def update_world_display(self, index):
        self.state.filter = FilterName(index)
        self.update()
