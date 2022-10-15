from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM


def test_conditional_read_d_reg_reg_off_not(hexagon):
    mem = RAM(8)
    mem.write(0, 8, b'\x00\x11\x22\x33\x44\x55\x66\x77')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000028))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\xc0\x31')
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x33221100
    assert hexagon.registers.general[3] == 0x77665544


def test_conditional_read_d_reg_reg_off_not_false(hexagon):
    mem = RAM(8)
    mem.write(0, 8, b'\x00\x11\x22\x33\x44\x55\x66\x77')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000028))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\xc0\x31')
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0
    assert hexagon.registers.general[3] == 0
