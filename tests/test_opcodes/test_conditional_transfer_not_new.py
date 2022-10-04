from tests.test_opcodes.common import set_predicate, HookedXunits


def test_conditional_transfer_not_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc0\xff\x8f\x7e')
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xfffffffe


def test_conditional_transfer_not_new_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc0\xff\x8f\x7e')
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0


def test_conditional_transfer_not_new_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0f\xc0\xff\x8f\x7e')
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xf000003e
