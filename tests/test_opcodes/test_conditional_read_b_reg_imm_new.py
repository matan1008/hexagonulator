from tests.test_opcodes.common import set_predicate, HookedXunits, add_memory


def test_conditional_read_b_reg_imm_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x00\x43')
    add_memory(hexagon, b'\xf0\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x4000001f
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffffff0


def test_conditional_read_b_reg_imm_new_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x00\x43')
    add_memory(hexagon, b'\xf0\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x4000001f
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0


def test_conditional_read_b_reg_imm_new_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x21\xc0\x00\x43')
    add_memory(hexagon, b'\xf0\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x1f
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffffff0
