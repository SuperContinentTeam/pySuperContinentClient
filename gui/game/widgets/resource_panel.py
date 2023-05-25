from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

from utils.size import GAME_WIDTH, RESOURCE_ITEM_HEIGHT, GAME_TOP, GAME_LEFT, DX
from utils.reference import format_number, image
from utils.colors import BLACK, WHITE, RED


class ResourceItemPanel:
    def __init__(self, name, storage=999999999999, monthly=99999):
        self.name = name
        self.storage = storage
        self.monthly = monthly


class ResourcePanel:
    items = ("energy", "mineral", "food", "customer",
             "alloy", "physics", "engineer", "beyond")

    def __init__(self):
        for item in self.items:
            setattr(self, item, ResourceItemPanel(item))

    def init(self, arguments: dict):
        for item in self.items:
            if arg := arguments.get(item):
                setattr(getattr(self, item), "storage", arg["storage"])
                setattr(getattr(self, item), "monthly", arg["monthly"])

    def draw(self, painter: QPainter):
        item_width = GAME_WIDTH // len(self.items)
        flags = Qt.AlignLeft | Qt.AlignVCenter

        painter.setPen(BLACK)
        painter.setBrush(WHITE)
        for i, item in enumerate(self.items):
            start_x = item_width * i + GAME_LEFT

            painter.drawRect(
                start_x,
                GAME_TOP,
                item_width,
                RESOURCE_ITEM_HEIGHT
            )
            painter.drawPixmap(
                start_x,
                GAME_TOP,
                RESOURCE_ITEM_HEIGHT,
                RESOURCE_ITEM_HEIGHT,
                image(item)
            )

            r: ResourceItemPanel = getattr(self, item)
            if r.monthly < 0:
                painter.setPen(RED)

            painter.drawText(
                start_x + RESOURCE_ITEM_HEIGHT + DX * 5,
                GAME_TOP,
                item_width - RESOURCE_ITEM_HEIGHT,
                RESOURCE_ITEM_HEIGHT // 2,
                flags,
                format_number(r.storage)
            )

            painter.drawText(
                start_x + RESOURCE_ITEM_HEIGHT + DX * 5,
                GAME_TOP + RESOURCE_ITEM_HEIGHT // 2,
                item_width - RESOURCE_ITEM_HEIGHT,
                RESOURCE_ITEM_HEIGHT // 2,
                flags,
                format_number(r.monthly, True)
            )

            if r.monthly < 0:
                painter.setPen(BLACK)
