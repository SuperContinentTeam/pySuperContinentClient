# from PyQt5.QtCore import QTimer
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QPushButton, QLabel, QWidget, QLineEdit
# from PyQt5.QtCore import

from utils.settings import TITLE


class SingleSettingWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.last_window = self.parent()
        pos = self.last_window.pos()

        self.setWindowTitle(TITLE)
        self.setGeometry(pos.x(), pos.y(), 400, 300)

        layout = QGridLayout()
        layout.addWidget(QLabel("世界宽度"), 0, 0)
        layout.addWidget(QLineEdit(""), 0, 1)
        layout.addWidget(QLabel("AI数量"), 1, 0)
        layout.addWidget(QLineEdit(""), 1, 1)
        layout.addWidget(QLabel("(未启用)"), 1, 2)
        layout.addWidget(QLabel("资源比例"), 2, 0)
        layout.addWidget(QLineEdit(""), 2, 1)
        layout.addWidget(QLabel("国家名称"), 3, 0)
        layout.addWidget(QLineEdit(""), 3, 1)
        layout.addWidget(QLabel("启用AI"), 4, 0)
        layout.addWidget(QLineEdit(""), 4, 1)
        layout.addWidget(QLabel("(未启用)"), 4, 2)
        layout.addWidget(QLabel("导入AI模型"), 5, 0)
        layout.addWidget(QLineEdit(""), 5, 1)
        layout.addWidget(QPushButton("打开文件", self), 5, 2)


        btn_back = QPushButton("返回", self)
        btn_back.clicked.connect(self.close_window)
        layout.addWidget(btn_back, 6, 2)

        layout.addWidget(QPushButton("开始", self), 7, 2)

        center_widget = QWidget(self)
        center_widget.setLayout(layout)
        self.setCentralWidget(center_widget)


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.last_window.show()

        return super().closeEvent(a0)
    
    def close_window(self):
        self.close()

    #     self.timer = QTimer(self)
    #     self.tick = 1

    #     self.timer.timeout.connect(self.receiver_from_server)
    #     self.timer.start(1000)

    # def receiver_from_server(self):
    #     print("Hello world", self.tick)
    #     self.tick += 1


# 绘制图片
# img = QImage("xxx.png")
# rect = QRect(x, y, img.width()/2, img.height()/2)
# painter.drawImage(rect, img)
