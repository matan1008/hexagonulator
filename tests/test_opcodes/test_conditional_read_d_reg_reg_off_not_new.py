from tests.test_opcodes.common import set_predicate, HookedXunits, add_memory


def test_conditional_read_d_reg_reg_off_not_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\xc0\x33')
    add_memory(hexagon, b'\x00\x11\x22\x33\x44\x55\x66\x77', 0x40000020)
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x33221100
    assert hexagon.registers.general[3] == 0x77665544


def test_conditional_read_d_reg_reg_off_not_new_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\xc0\x33')
    add_memory(hexagon, b'\x00\x11\x22\x33\x44\x55\x66\x77', 0x40000020)
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0
    assert hexagon.registers.general[3] == 0
