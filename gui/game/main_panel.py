from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtGui import QPainter, QPaintEvent

from gui.game.widgets.resource_panel import ResourcePanel

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

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        self.resource_panel.draw(painter)

    def closeEvent(self, a0) -> None:
        if self.last_window:
            self.last_window.show()

        return super().closeEvent(a0)

    def center(self):
        # 获取屏幕的大�?
        screen = QDesktopWidget().screenGeometry()
        # 计算窗口居中时的左上角位�?
        x = (screen.width() - WIDTH) // 2
        y = (screen.height() - HEIGHT) // 2
        # 移动窗口到居中位�?
        self.move(x, y)

