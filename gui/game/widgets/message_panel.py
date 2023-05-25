from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPlainTextEdit

from utils.size import GAME_WIDTH, MESSAGE_BOX_HEIGHT, WORLD_HEIGHT, GAME_LEFT, GAME_BOTTOM
from utils.colors import BLACK, WHITE, RED

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
