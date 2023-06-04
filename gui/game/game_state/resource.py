class Resource:
    def __init__(self, name, storage=0, produce=0):
        self.name = name
        self.storage = storage
        self.produce = produce

    def time_flow(self):
        self.storage += self.produce

    def update(self, p):
        self.produce += p
