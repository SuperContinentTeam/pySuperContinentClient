from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter

from utils.colors import BLACK, WHITE, RED
from utils.reference import image, FLAG_ALIGN_LEFT, format_number
from utils.size import GAME_WIDTH, RESOURCE_ITEM_HEIGHT, GAME_TOP, GAME_LEFT, DX, GAME_RIGHT


class ResourceItem:
    def __init__(self, name, storage=0, monthly=0):
        self.name = name
        self.storage = storage
        self.monthly = monthly


class ResourceWidget(QWidget):
    items = ("energy", "mineral", "food", "customer",
             "alloy", "physics", "engineer", "beyond")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_width = GAME_WIDTH // len(self.items)

        for item in self.items:
            setattr(self, item, ResourceItem(item))

        self.setGeometry(GAME_TOP, GAME_LEFT, GAME_WIDTH, RESOURCE_ITEM_HEIGHT)

    def init(self, arguments: dict):
        for item in self.items:
            if arg := arguments.get(item):
                setattr(getattr(self, item), "storage", arg["storage"])
                setattr(getattr(self, item), "monthly", arg["monthly"])

    def paintEvent(self, a0):
        painter = QPainter()
        painter.setPen(BLACK)
        painter.setBrush(WHITE)

        for i, item in enumerate(self.items):
            r: ResourceItem = getattr(self, item)
            start_x = self.item_width * i + GAME_LEFT

            painter.drawRect(
                start_x,
                GAME_TOP,
                self.item_width,
                RESOURCE_ITEM_HEIGHT
            )

            painter.drawPixmap(
                start_x,
                GAME_TOP,
                RESOURCE_ITEM_HEIGHT,
                RESOURCE_ITEM_HEIGHT,
                image(r.name)
            )

            if r.monthly < 0:
                painter.setPen(RED)

            painter.drawText(
                start_x + RESOURCE_ITEM_HEIGHT + DX * 5,
                GAME_TOP,
                self.item_width - RESOURCE_ITEM_HEIGHT,
                RESOURCE_ITEM_HEIGHT // 2,
                FLAG_ALIGN_LEFT,
                format_number(r.storage)
            )

            painter.drawText(
                start_x + RESOURCE_ITEM_HEIGHT + DX * 5,
                GAME_TOP + RESOURCE_ITEM_HEIGHT // 2,
                self.item_width - RESOURCE_ITEM_HEIGHT,
                RESOURCE_ITEM_HEIGHT // 2,
                FLAG_ALIGN_LEFT,
                format_number(r.monthly, True)
            )

            if r.monthly < 0:
                painter.setPen(BLACK)
