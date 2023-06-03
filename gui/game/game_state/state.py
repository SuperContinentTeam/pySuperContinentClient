# 全局状态
from typing import Tuple, Dict

from PyQt6.QtCore import QObject, pyqtSignal

from gui.game.game_state.block import Block


class StateSignal(QObject):
    click_world_block = pyqtSignal(tuple)


class GameState:
    __instance = None
    signals = StateSignal()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


    def __init__(self, ws=10):
        self.world_size = ws
        self.world_map: Dict[Tuple[int, int], Block] = {
            (i, j): Block(i, j)
            for i in range(ws) for j in range(ws)
        }
