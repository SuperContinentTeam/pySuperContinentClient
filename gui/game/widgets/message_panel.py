from PyQt5.QtWidgets import QPlainTextEdit

from utils.size import MESSAGE_BOX_HEIGHT, WORLD_HEIGHT, GAME_LEFT, GAME_BOTTOM


class MessageBoxPanel:
    def __init__(self, parent):
        self.parent = parent
        self.plain_text = QPlainTextEdit(parent)

        self.plain_text.setGeometry(
            GAME_LEFT,
            GAME_BOTTOM - MESSAGE_BOX_HEIGHT,
            WORLD_HEIGHT,
            MESSAGE_BOX_HEIGHT
        )
