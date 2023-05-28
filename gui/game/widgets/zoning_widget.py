from typing import Dict, Tuple, Iterable

from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QRect


from utils.size import ZONING_LEFT, ZONING_TOP, ZONING_HEIGHT
from utils.colors import BLACK, WHITE
from utils.reference import FLAG_ALIGN_CENTER

from gui.game.widgets.world_panel import Block


class ZoningBlock:
    def __init__(self, c, r, block: Block):
        self.ix = c
        self.iy = r
        self.block = block
