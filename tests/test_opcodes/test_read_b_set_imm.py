from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM


def test_read_b_set_imm(hexagon):
    mem = RAM(8)
    mem.write(0, 4, b'\xf0\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x20, end=0x24))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xd8\x00\x9b')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x20
    assert hexagon.registers.general[1] == 0xfffffff0


def test_read_b_set_imm_apply_extension(hexagon):
    mem = RAM(8)
    mem.write(0, 4, b'\xf0\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x01\xd8\x00\x9b')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x40000020
    assert hexagon.registers.general[1] == 0xfffffff0
