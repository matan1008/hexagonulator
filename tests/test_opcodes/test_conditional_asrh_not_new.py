from tests.test_opcodes.common import HookedXunits, set_predicate


def test_conditional_asrh_not_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xec\x20\x70')
    hexagon.registers.general[0] = 0xf0000000
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffff000


def test_conditional_asrh_not_new_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xec\x20\x70')
    hexagon.registers.general[0] = 0xf0000000
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0
