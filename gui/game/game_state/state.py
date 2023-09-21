import random
from typing import Tuple, Dict, Iterable
from collections import defaultdict

from PyQt6.QtCore import QObject, pyqtSignal

from gui.game.game_state.elements import Block, ZoningBlock
from gui.game.game_state.player import Player
from gui.game.game_state.reference import FilterName, ResourceList
from gui.game.game_state.resource import Resource
from utils.reference import BLOCK_ENV_LIST
from utils.weights import BlockEnvWidget


# 初始化玩家
def initial_player(world_map: Iterable[Block], number):
    choices_blocks = [block for block in world_map if block.env == 0]
    choices_blocks = random.choices(choices_blocks, k=number)
    players = list()
    for i in range(number):
        player = Player(str(i))
        block = choices_blocks[i]
        # 玩家地块区划尺寸默认为 4
        block.zoning_number = 4
        player.add_block(block)
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


# 初始化资源
def initial_resource(items: Iterable):
    return {item: Resource(item) for item in items}


class StateSignal(QObject):
    click_world_block = pyqtSignal(tuple)
    click_filter_panel = pyqtSignal(int)


class GameState:
    __instance = None
    signals = StateSignal()
    arguments = dict()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, ws=10):
        self.world_size = ws
        self.world_map = initial_world(ws)

        blocks = self.world_map.values()
        self.players = initial_player(blocks, 1)

        self.zoning_map = initial_zoning(blocks)

        self.filter = FilterName.PLAYER  # 领土滤镜

        self.resource_map = initial_resource(ResourceList)


class State:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, arguments=None):
        self.name = arguments["name"]
