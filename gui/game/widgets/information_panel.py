from PyQt6.QtWidgets import QTextBrowser

from utils.size import INFORMATION_LEFT, INFORMATION_WIDTH, INFORMATION_HEIGHT, INFORMATION_TOP


class InformationPanel(QTextBrowser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(
            INFORMATION_LEFT,
            INFORMATION_TOP,
            INFORMATION_WIDTH,
            INFORMATION_HEIGHT
        )

        for i in range(3):
            self.append("<h2>hello world</h2>")
