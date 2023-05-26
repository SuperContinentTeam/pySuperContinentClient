import random


class Block:
    def __init__(self, c, r):
        self.ix = c
        self.iy = r
        self.zoning_number = random.randint(3, 6)

    def __str__(self) -> str:
        return f"<Block: {self.ix}, {self.iy}>"
