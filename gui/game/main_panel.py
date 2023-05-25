from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from utils.settings import TITLE, CommonSize



class MainGamePanel(QMainWindow):
    def __init__(self, argumensts, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_window = self.parent()
        self.arguments = argumensts

        self.setWindowTitle(TITLE)
        self.resize(CommonSize.WIDTH, CommonSize.HEIGHT)
        self.center()

    def closeEvent(self, a0) -> None:
        if self.last_window:
            self.last_window.show()

        return super().closeEvent(a0)
    
    def center(self):
        # 获取屏幕的大小
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口的大小
        window_size = self.geometry()
        # 计算窗口居中时的左上角位置
        x = (screen.width() - window_size.width()) // 2
        y = (screen.height() - window_size.height()) // 2
        # 移动窗口到居中位置
        self.move(x, y)