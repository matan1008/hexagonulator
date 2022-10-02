from tests.test_opcodes.common import HookedXunits, set_predicate


def test_conditional_add_not_new_reg(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xe1\x00\xfb')
    hexagon.registers.general[0] = 4
    hexagon.registers.general[1] = 3
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[2] == 7


def test_conditional_add_not_new_reg_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xe1\x00\xfb')
    hexagon.registers.general[0] = 4
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0
