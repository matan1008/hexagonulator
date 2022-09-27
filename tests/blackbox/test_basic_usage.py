from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM
from hexgonulator.v67.processor import HexagonV67


def test_add():
    mem = RAM(8)
    mem.write(0, 8, b'\xc0\x40\x00\xb0\xe1\xc0\x00\xb0')
    proc = HexagonV67()
    proc.registers.general[0] = 3
    proc.memory.controllers.append(MemoryController(mem, start=0, end=8))
    proc.cycle()
    assert proc.registers.general[0] == 9
    assert proc.registers.general[1] == 10
