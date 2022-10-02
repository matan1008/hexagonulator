from tests.test_opcodes.common import HookedXunits, set_predicate


def test_conditional_add_new_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc1\xff\x00\x74')
    hexagon.registers.general[0] = 4
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 2


def test_conditional_add_new_imm_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc1\xff\x00\x74')
    hexagon.registers.general[0] = 4
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0


def test_conditional_add_new_imm_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0f\xc1\xff\x00\x74')
    hexagon.registers.general[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xf000003f
