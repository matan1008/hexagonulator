from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM


def test_read_b_inc_reg_brev(hexagon):
    mem = RAM(8)
    mem.write(0, 4, b'\xf0\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\x00\x9f')
    hexagon.registers.general[0] = 0x40000400
    hexagon.registers.m0.value = 0x20
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffffff0
    assert hexagon.registers.general[0] == 0x40000420
