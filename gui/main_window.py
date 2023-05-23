from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timer = QTimer(self)
        self.tick = 1

        self.timer.timeout.connect(self.receiver_from_server)
        self.timer.start(1000)

    def receiver_from_server(self):
        print("Hello world", self.tick)
        self.tick += 1
