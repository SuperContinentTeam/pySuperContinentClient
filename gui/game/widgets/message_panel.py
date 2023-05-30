from PyQt6.QtWidgets import QTextBrowser

from utils.size import MESSAGE_BOX_LEFT, MESSAGE_BOX_TOP, MESSAGE_BOX_WIDTH, MESSAGE_BOX_HEIGHT


class MessageBoxPanel(QTextBrowser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(
            MESSAGE_BOX_LEFT,
            MESSAGE_BOX_TOP,
            MESSAGE_BOX_WIDTH,
            MESSAGE_BOX_HEIGHT
        )

        for i in range(3):
            self.append("<h2>hello world</h2>")
