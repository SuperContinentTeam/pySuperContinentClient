from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget

from utils.colors import BLACK, WHITE, RED
from utils.reference import image, FLAG_ALIGN_LEFT, format_number
from utils.size import GAME_WIDTH, RESOURCE_HEIGHT, GAME_TOP, GAME_LEFT


class ResourceItem:
    def __init__(self, name, storage=0, monthly=0):
        self.name = name
        self.storage = storage
        self.monthly = monthly


class ResourcePanel:
    items = ("energy", "mineral", "food", "customer",
             "alloy", "physics", "engineer", "beyond")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_width = GAME_WIDTH // len(self.items)

        for item in self.items:
            setattr(self, item, ResourceItem(item))

    def init(self, arguments: dict):
        for item in self.items:
            if arg := arguments.get(item):
                setattr(getattr(self, item), "storage", arg["storage"])
                setattr(getattr(self, item), "monthly", arg["monthly"])

    def draw(self, painter: QPainter):
        painter.setPen(BLACK)
        painter.setBrush(WHITE)

        for i, item in enumerate(self.items):
            r: ResourceItem = getattr(self, item)
            start_x = self.item_width * i + GAME_LEFT

            painter.drawRect(
                start_x,
                GAME_TOP,
                self.item_width,
                RESOURCE_HEIGHT
            )

            painter.drawPixmap(
                start_x,
                GAME_TOP,
                RESOURCE_HEIGHT,
                RESOURCE_HEIGHT,
                image(r.name)
            )

            if r.monthly < 0:
                painter.setPen(RED)

            painter.drawText(
                start_x + RESOURCE_HEIGHT + 5,
                GAME_TOP,
                self.item_width - RESOURCE_HEIGHT,
                RESOURCE_HEIGHT // 2,
                FLAG_ALIGN_LEFT,
                format_number(r.storage)
            )

            painter.drawText(
                start_x + RESOURCE_HEIGHT + 5,
                GAME_TOP + RESOURCE_HEIGHT // 2,
                self.item_width - RESOURCE_HEIGHT,
                RESOURCE_HEIGHT // 2,
                FLAG_ALIGN_LEFT,
                format_number(r.monthly, True)
            )

            if r.monthly < 0:
                painter.setPen(BLACK)

    def click(self, x, button) -> None:
        name = self.items[x // self.item_width]
        click = "Left" if button == Qt.MouseButton.LeftButton else "Right"
        print(f"{click} click in: {name}")
