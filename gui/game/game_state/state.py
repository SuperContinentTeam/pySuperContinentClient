# 全局状态
from typing import Tuple, Dict

from gui.game.game_state.block import Block


class GameState:
    def __init__(self, ws):
        self.world_size = ws
        self.world_map: Dict[Tuple[int, int], Block] = {
            (i, j): Block(i, j)
            for i in range(ws) for j in range(ws)
        }
