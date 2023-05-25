from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QPoint

from utils.size import GAME_WIDTH, RESOURCE_ITEM_HEIGHT, GAME_TOP, GAME_LEFT, DX, GAME_RIGHT
from utils.reference import format_number, image
from utils.colors import BLACK, WHITE, RED


class ResourceItemPanel:
    def __init__(self, name, storage=999999999999, monthly=99999):
        self.name = name
        self.storage = storage
        self.monthly = monthly

    def draw(self, painter: QPainter, start_x: int, width: int, flag):
        painter.drawRect(
            start_x,
            GAME_TOP,
            width,
            RESOURCE_ITEM_HEIGHT
        )

        painter.drawPixmap(
            start_x,
            GAME_TOP,
            RESOURCE_ITEM_HEIGHT,
            RESOURCE_ITEM_HEIGHT,
            image(self.name)
        )

        if self.monthly < 0:
            painter.setPen(RED)

        painter.drawText(
            start_x + RESOURCE_ITEM_HEIGHT + DX * 5,
            GAME_TOP,
            width - RESOURCE_ITEM_HEIGHT,
            RESOURCE_ITEM_HEIGHT // 2,
            flag,
            format_number(self.storage)
        )

        painter.drawText(
            start_x + RESOURCE_ITEM_HEIGHT + DX * 5,
            GAME_TOP + RESOURCE_ITEM_HEIGHT // 2,
            width - RESOURCE_ITEM_HEIGHT,
            RESOURCE_ITEM_HEIGHT // 2,
            flag,
            format_number(self.monthly, True)
        )

        if self.monthly < 0:
            painter.setPen(BLACK)


class ResourcePanel:
    items = ("energy", "mineral", "food", "customer",
             "alloy", "physics", "engineer", "beyond")

    def __init__(self):
        for item in self.items:
            setattr(self, item, ResourceItemPanel(item))

        self.item_width = GAME_WIDTH // len(self.items)

    def init(self, arguments: dict):
        for item in self.items:
            if arg := arguments.get(item):
                setattr(getattr(self, item), "storage", arg["storage"])
                setattr(getattr(self, item), "monthly", arg["monthly"])

    def check_in(self, x, y):
        b1 = GAME_TOP < y < GAME_TOP + RESOURCE_ITEM_HEIGHT
        b2 = GAME_LEFT < x < GAME_RIGHT
        return b1 and b2

    def click(self, x, y, button: Qt.MouseButton):
        if not self.check_in(x, y):
            return
        
        name = self.items[x // self.item_width]
        click = "Left" if button == Qt.LeftButton else "Right"
        print(f"{click} click in: {name}")


    def draw(self, painter: QPainter):
        flag = Qt.AlignLeft | Qt.AlignVCenter

        painter.setPen(BLACK)
        painter.setBrush(WHITE)

        for i, item in enumerate(self.items):
            start_x = self.item_width * i + GAME_LEFT
            r: ResourceItemPanel = getattr(self, item)
            r.draw(painter, start_x, self.item_width, flag)



