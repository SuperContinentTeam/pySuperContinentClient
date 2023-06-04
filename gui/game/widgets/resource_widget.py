from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter

from gui.game.game_state.reference import ResourceList
from gui.game.game_state.resource import Resource
from gui.game.game_state.state import GameState
from utils.colors import BLACK, WHITE, RED
from utils.reference import image, FLAG_ALIGN_LEFT, format_number
from utils.size import GAME_WIDTH, RESOURCE_HEIGHT


class ResourcePanel:
    state = GameState()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_width = GAME_WIDTH // len(ResourceList)

    def draw(self, painter: QPainter):
        painter.setPen(BLACK)
        painter.setBrush(WHITE)
        for i, item in enumerate(ResourceList):
            r: Resource = self.state.resource_map[item]
            start_x = self.item_width * i

            painter.drawRect(
                start_x,
                0,
                self.item_width,
                RESOURCE_HEIGHT
            )

            painter.drawPixmap(
                start_x,
                0,
                RESOURCE_HEIGHT,
                RESOURCE_HEIGHT,
                image(r.name)
            )

            if r.produce < 0:
                painter.setPen(RED)

            painter.drawText(
                start_x + RESOURCE_HEIGHT + 5,
                0,
                self.item_width - RESOURCE_HEIGHT,
                RESOURCE_HEIGHT // 2,
                FLAG_ALIGN_LEFT,
                format_number(r.storage)
            )

            painter.drawText(
                start_x + RESOURCE_HEIGHT + 5,
                0 + RESOURCE_HEIGHT // 2,
                self.item_width - RESOURCE_HEIGHT,
                RESOURCE_HEIGHT // 2,
                FLAG_ALIGN_LEFT,
                format_number(r.produce, True)
            )

            if r.produce < 0:
                painter.setPen(BLACK)

    def click(self, x, button) -> None:
        name = ResourceList[x // self.item_width]
        click = "Left" if button == Qt.MouseButton.LeftButton else "Right"
        print(f"{click} click in: {name}")
