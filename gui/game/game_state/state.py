import random
from typing import Tuple, Dict, Iterable
from collections import defaultdict

from PyQt6.QtCore import QObject, pyqtSignal

from gui.game.game_state.elements import Block, ZoningBlock
from gui.game.game_state.player import Player
from gui.game.game_state.reference import FilterName
from utils.reference import BLOCK_ENV_LIST
from utils.weights import BlockEnvWidget


# 初始化玩家
def initial_player(world_map: Iterable[Block], number):
    choices_blocks = random.choices([block for block in world_map if block.env == 0], k=number)
    players = list()
    for i in range(number):
        player = Player(str(i))
        player.add_block(choices_blocks[i])
        players.append(player)

    return players


# 初始化世界地图
def initial_world(world_size) -> Dict[Tuple[int, int], Block]:
    # 按权重获取地块环境值
    environments = random.choices(BLOCK_ENV_LIST, weights=BlockEnvWidget, k=world_size * world_size)
    result: Dict[Tuple[int, int], Block] = dict()
    for i in range(world_size):
        for j in range(world_size):
            result[(i, j)] = Block(i, j, environments[i * world_size + j])

    return result


# 初始化地块的区划
def initial_zoning(blocks: Iterable[Block]) -> Dict[Block, Dict[Tuple[int, int], ZoningBlock]]:
    result: Dict[Block, Dict[Tuple[int, int], ZoningBlock]] = defaultdict(dict)
    for block in blocks:
        result[block] = {
            (i, j): ZoningBlock(i, j, block)
            for i in range(block.zoning_number) for j in range(block.zoning_number)
        }

    return result


class StateSignal(QObject):
    click_world_block = pyqtSignal(tuple)
    click_filter_panel = pyqtSignal(int)


class GameState:
    __instance = None
    signals = StateSignal()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, ws=10):
        self.world_size = ws
        self.world_map = initial_world(ws)

        blocks = self.world_map.values()
        self.zoning_map = initial_zoning(blocks)
        self.players = initial_player(blocks, 1)
        self.filter = FilterName.DISCOVER  # 探索滤镜
