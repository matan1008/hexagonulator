from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM


def test_memb_fifo_inc_reg_brev(hexagon):
    mem = RAM(4)
    mem.write(0, 4, b'\x77\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\x80\x9e')
    hexagon.registers.general[0] = 0x40000400
    hexagon.registers.general[1] = 0x221100ff
    hexagon.registers.general[2] = 0x66554433
    hexagon.registers.m0.value = 0x20
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x40000420
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
