def test_cmp_gt_new_jump_reg_hint(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x01\x40\x60\x70\xfe\xe2\xb2\x20')
    hexagon.registers.general[0] = 2
    hexagon.registers.general[2] = 0xfffffffe
    hexagon.cycle()
    assert hexagon.registers.npc == pc - 4


def test_cmp_gt_new_jump_reg_hint_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x01\x40\x60\x70\xfe\xe2\xb2\x20')
    hexagon.registers.general[0] = 0
    hexagon.registers.general[2] = 1
    hexagon.cycle()
    assert hexagon.registers.npc == pc + 8


def test_cmp_gt_new_jump_reg_hint_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 12, b'\x01\x40\x60\x70\x00\x40\x00\x01\x02\xe2\x82\x20')
    hexagon.registers.general[0] = 2
    hexagon.registers.general[2] = 0xfffffffe
    hexagon.cycle()
    assert hexagon.registers.npc == pc + 0x10000004
