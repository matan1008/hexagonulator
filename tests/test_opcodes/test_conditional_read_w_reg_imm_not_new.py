from tests.test_opcodes.common import set_predicate, HookedXunits, add_memory


def test_conditional_read_w_reg_imm_not_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x80\x47')
    add_memory(hexagon, b'\x44\x33\x22\x11', 0x40000020)
    hexagon.registers.general[0] = 0x4000001c
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x11223344


def test_conditional_read_w_reg_imm_not_new_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x80\x47')
    add_memory(hexagon, b'\x44\x33\x22\x11', 0x40000020)
    hexagon.registers.general[0] = 0x4000001c
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0


def test_conditional_read_w_reg_imm_not_new_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x21\xc0\x80\x47')
    add_memory(hexagon, b'\x44\x33\x22\x11', 0x40000020)
    hexagon.registers.general[0] = 0x1c
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x11223344
