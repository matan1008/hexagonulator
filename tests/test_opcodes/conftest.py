import pytest

from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM
from hexgonulator.v67.processor import HexagonV67

OPCODE_ADDR = 0x80000000


@pytest.fixture()
def hexagon():
    mem = RAM(0x10)
    proc = HexagonV67()
    proc.memory.controllers.append(MemoryController(mem, start=OPCODE_ADDR, end=OPCODE_ADDR + 0x10))
    proc.registers.pc = OPCODE_ADDR
    proc.registers.npc_to_pc()
    return proc
