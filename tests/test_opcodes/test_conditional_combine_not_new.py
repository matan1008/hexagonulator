from tests.test_opcodes.common import set_predicate, HookedXunits


def test_conditional_combine_not_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xe1\x00\xfd')
    hexagon.registers.general[0] = 0x55667788
    hexagon.registers.general[1] = 0x11223344
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x11223344
    assert hexagon.registers.general[3] == 0x55667788


def test_conditional_combine_not_new_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xe1\x00\xfd')
    hexagon.registers.general[0] = 0x55667788
    hexagon.registers.general[1] = 0x11223344
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0
    assert hexagon.registers.general[3] == 0
