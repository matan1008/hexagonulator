from tests.test_opcodes.common import set_predicate, HookedXunits


def test_conditional_sub_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xe1\x20\xfb')
    hexagon.registers.general[0] = 5
    hexagon.registers.general[1] = 9
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[2] == 4


def test_conditional_sub_new_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xe1\x20\xfb')
    hexagon.registers.general[0] = 5
    hexagon.registers.general[1] = 9
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0
