from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM
from tests.test_opcodes.common import set_predicate, HookedXunits


def test_conditional_read_b_reg_reg_off_not_new(hexagon):
    mem = RAM(8)
    mem.write(0, 4, b'\xf0\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\x00\x33')
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0xfffffff0


def test_conditional_read_b_reg_reg_off_not_new_false(hexagon):
    mem = RAM(8)
    mem.write(0, 4, b'\xf0\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\x00\x33')
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0
