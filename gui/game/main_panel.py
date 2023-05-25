from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtGui import QPainter, QPaintEvent, QMouseEvent
from PyQt5.QtCore import Qt
from gui.game.widgets.message_panel import MessageBoxPanel
from gui.game.widgets.resource_panel import ResourcePanel
from gui.game.widgets.world_panel import WorldPanel

from utils.settings import TITLE
from utils.size import WIDTH, HEIGHT


class MainGamePanel(QMainWindow):
    def __init__(self, argumensts, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_window = self.parent()
        # 初始参数
        self.arguments = argumensts

        self.setWindowTitle(TITLE)
        self.resize(WIDTH, HEIGHT)
        self.center()

        # 资源板块
        self.resource_panel = ResourcePanel()
        # 消息板块
        # self.message_box = MessageBoxPanel(self)
        # 世界板块
        self.world = WorldPanel()

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        self.resource_panel.draw(painter)
        self.world.draw(painter)

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        pos = a0.pos()
        button = a0.button()
        x, y = pos.x(), pos.y()
        
        self.resource_panel.click(x, y, button)
        self.world.click(x, y, button)

    def closeEvent(self, a0) -> None:
        if self.last_window:
            self.last_window.show()

        return super().closeEvent(a0)

    def center(self):
        screen = QDesktopWidget().screenGeometry()

        x = (screen.width() - WIDTH) // 2
        y = (screen.height() - HEIGHT) // 2

        self.move(x, y)



