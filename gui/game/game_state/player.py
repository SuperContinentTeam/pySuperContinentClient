from gui.game.game_state.elements import Block
from utils.colors import RED


class Player:
    def __init__(self, name, color=RED):
        self.name = name
        self.blocks = set()
        self.color = color

    def add_block(self, block: Block):
        block.player = self
        self.blocks.add(block)

    def lost_block(self, block: Block):
        block.player = None
        self.blocks.remove(block)
