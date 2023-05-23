from PyQt5.QtWidgets import QMainWindow
from utils.settings import TITLE

class StartWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle(TITLE)
        self.setGeometry(300,300,400,300)