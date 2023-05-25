from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QApplication
from utils.settings import TITLE

from gui.single_setting_window import SingleSettingWindow


class StartWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle(TITLE)
        self.setGeometry(300, 300, 400, 300)

        v_box = QVBoxLayout()

        btn_single = QPushButton("单人模式", self)
        btn_single.clicked.connect(self.open_single_window)

        btn_multi = QPushButton("多人模式", self)
        btn_setting = QPushButton("游戏设置", self)

        btn_quit = QPushButton("退出游�?, self)
        btn_quit.clicked.connect(QApplication.quit)

        v_box.addWidget(btn_single)
        v_box.addWidget(btn_multi)
        v_box.addWidget(btn_setting)
        v_box.addWidget(btn_quit)

        center_widget = QWidget(self)
        center_widget.setLayout(v_box)
        self.setCentralWidget(center_widget)

    def open_single_window(self):
        self.hide()
        next_window = SingleSettingWindow(self)
        next_window.show()



