from tests.test_opcodes.common import set_predicate, HookedXunits


def test_conditional_sxth_not_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xec\xe0\x70')
    hexagon.registers.general[0] = 0x0000f000
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffff000


def test_conditional_sxth_not_new_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xec\xe0\x70')
    hexagon.registers.general[0] = 0x0000f000
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0
