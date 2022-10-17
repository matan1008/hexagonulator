from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM
from hexgonulator.v67.xunits import Xunits


class HookedXunits(Xunits):
    def __init__(self, processor, last_cycle_hook):
        super().__init__(processor)
        self.last_cycle_hook = last_cycle_hook

    def cycle(self):
        for i in range(3):
            if i == 2:
                self.last_cycle_hook()
            for unit in self.units[::-1]:
                if unit is None:
                    continue
                next(unit)


def set_predicate(hexagon, value):
    hexagon.registers.predicate[0] = value


def add_memory(hexagon, data, address):
    mem = RAM(len(data))
    mem.write(0, len(data), data)
    hexagon.memory.controllers.append(MemoryController(mem, start=address, end=address + len(data)))
