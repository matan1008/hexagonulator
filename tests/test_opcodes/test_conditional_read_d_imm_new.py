from tests.test_opcodes.common import set_predicate, HookedXunits, add_memory


def test_conditional_read_d_imm_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x80\xf0\xd0\x9f')
    add_memory(hexagon, b'\x00\x11\x22\x33\x44\x55\x66\x77', 0x20)
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x33221100
    assert hexagon.registers.general[1] == 0x77665544


def test_conditional_read_d_imm_new_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x80\xf0\xd0\x9f')
    add_memory(hexagon, b'\x00\x11\x22\x33\x44\x55\x66\x77', 0x20)
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0
    assert hexagon.registers.general[1] == 0


def test_conditional_read_d_imm_new_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x80\xf0\xd0\x9f')
    add_memory(hexagon, b'\x00\x11\x22\x33\x44\x55\x66\x77', 0x40000020)
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x33221100
    assert hexagon.registers.general[1] == 0x77665544
