import random


# 世界地块
class Block:
    def __init__(self, c, r, env):
        self.ix = c
        self.iy = r
        self.env = env
        self.visitable = True
        self.player = None

        self.zoning_number = random.randint(3, 6)

    def __str__(self) -> str:
        return f"<Block: {self.ix}, {self.iy}>"


# 地块区划
class ZoningBlock:
    def __init__(self, col, row, block: Block):
        self.ix = col
        self.iy = row
        self.block = block

    def __str__(self):
        return f"<Zoning: {self.ix}, {self.iy}>"
