from PyQt6.QtWidgets import QTextEdit

from utils.size import INPUT_LEFT, INPUT_TOP, INPUT_WIDTH, INPUT_HEIGHT


class TextInputPanel(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(
            INPUT_LEFT,
            INPUT_TOP,
            INPUT_WIDTH,
            INPUT_HEIGHT
        )

        self.setPlaceholderText("输入消息或指令，按回车键确认")
