from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM
from tests.test_opcodes.common import set_predicate, HookedXunits


def test_conditional_read_b_imm_new(hexagon):
    mem = RAM(8)
    mem.write(0, 4, b'\xf0\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x20, end=0x24))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x80\xf0\x10\x9f')
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xfffffff0


def test_conditional_read_b_imm_new_false(hexagon):
    mem = RAM(8)
    mem.write(0, 4, b'\xf0\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x20, end=0x24))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x80\xf0\x10\x9f')
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0


def test_conditional_read_b_imm_new_apply_extension(hexagon):
    mem = RAM(8)
    mem.write(0, 4, b'\xf0\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x80\xf0\x10\x9f')
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xfffffff0
