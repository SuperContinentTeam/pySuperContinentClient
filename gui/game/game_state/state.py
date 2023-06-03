# 全局状态
from typing import Tuple, Dict
from collections import defaultdict

from PyQt6.QtCore import QObject, pyqtSignal

from gui.game.game_state.elements import Block, ZoningBlock


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

        # 初始化世界地图
        self.world_map: Dict[Tuple[int, int], Block] = {
            (i, j): Block(i, j)
            for i in range(ws) for j in range(ws)
        }

        # 为每个地块初始化区划
        self.zoning_map: Dict[Block, Dict[Tuple[int, int], ZoningBlock]] = defaultdict(dict)
        for block in self.world_map.values():
            self.zoning_map[block] = {
                (i, j): ZoningBlock(i, j, block)
                for i in range(block.zoning_number) for j in range(block.zoning_number)
            }
