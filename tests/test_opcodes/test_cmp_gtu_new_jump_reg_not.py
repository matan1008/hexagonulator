def test_cmp_gtu_new_jump_reg_not(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x01\x40\x60\x70\xfe\xc2\x72\x21')
    hexagon.registers.general[0] = 0
    hexagon.registers.general[2] = 1
    hexagon.cycle()
    assert hexagon.registers.npc == pc - 4


def test_cmp_gtu_new_jump_reg_not_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x01\x40\x60\x70\xfe\xc2\x72\x21')
    hexagon.registers.general[0] = 0xfffffffe
    hexagon.registers.general[2] = 2
    hexagon.cycle()
    assert hexagon.registers.npc == pc + 8


def test_cmp_gtu_new_jump_reg_not_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 12, b'\x01\x40\x60\x70\x00\x40\x00\x01\x02\xc2\x42\x21')
    hexagon.registers.general[0] = 0
    hexagon.registers.general[2] = 1
    hexagon.cycle()
    assert hexagon.registers.npc == pc + 0x10000004
