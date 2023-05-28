from PyQt6.QtWidgets import QPlainTextEdit, QWidget

from utils.size import MESSAGE_BOX_HEIGHT, WORLD_HEIGHT, GAME_LEFT, GAME_BOTTOM


class MessageBoxPanel(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = self.parent()
        self.plain_text = QPlainTextEdit(self.parent)

        self.plain_text.setGeometry(
            GAME_LEFT,
            GAME_BOTTOM - MESSAGE_BOX_HEIGHT,
            WORLD_HEIGHT,
            MESSAGE_BOX_HEIGHT
        )
