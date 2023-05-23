# 指令队列
import asyncio
from typing import List


class Command:
    def __init__(self, tick, name, options: dict):
        self.name = name
        self.options = options
        self.tick = tick


class CommandQueue:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self):
        self.lock = asyncio.Lock()
        self.queue: List[Command] = list()

    @staticmethod
    def do_command(command: Command):
        print("执行命令: ", command)

    async def add_command(self, command: Command):
        async with self.lock:
            self.queue.append(command)

    async def run(self):
        while True:
            async with self.lock:
                for command in self.queue:
                    self.do_command(command)
                self.queue.clear()

            await asyncio.sleep(1)
