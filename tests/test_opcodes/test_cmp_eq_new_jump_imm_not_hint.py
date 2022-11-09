def test_cmp_eq_new_jump_imm_not_hint(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x01\x40\x60\x70\xfe\xe2\x72\x24')
    hexagon.registers.general[0] = 1
    hexagon.cycle()
    assert hexagon.registers.npc == pc - 4


def test_cmp_eq_new_jump_imm_not_hint_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x01\x40\x60\x70\xfe\xe2\x72\x24')
    hexagon.registers.general[0] = 2
    hexagon.cycle()
    assert hexagon.registers.npc == pc + 8


def test_cmp_eq_new_jump_imm_not_hint_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 12, b'\x01\x40\x60\x70\x00\x40\x00\x01\x02\xe2\x42\x24')
    hexagon.registers.general[0] = 1
    hexagon.cycle()
    assert hexagon.registers.npc == pc + 0x10000004
