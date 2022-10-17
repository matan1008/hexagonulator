from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM


def test_memb_fifo_inc_imm(hexagon):
    mem = RAM(4)
    mem.write(0, 4, b'\x77\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x80\x9a')
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.general[1] = 0x221100ff
    hexagon.registers.general[2] = 0x66554433
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x40000021
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
