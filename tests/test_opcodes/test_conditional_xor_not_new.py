from tests.test_opcodes.common import set_predicate, HookedXunits


def test_conditional_xor_not_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xe1\x60\xf9')
    hexagon.registers.general[0] = 0xffff0000
    hexagon.registers.general[1] = 0xff00ff00
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x00ffff00


def test_conditional_xor_not_new_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xe1\x60\xf9')
    hexagon.registers.general[0] = 0xffff0000
    hexagon.registers.general[1] = 0xff00ff00
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0
