def test_cmp_gt_and_jump_p0_reg(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xc8\xb0\x14')
    hexagon.registers.general[0] = 2
    hexagon.registers.general[16] = 0xfffffffe
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0xff
    assert hexagon.registers.npc == pc - 4


def test_cmp_gt_and_jump_p0_reg_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xc8\xb0\x14')
    hexagon.registers.general[0] = 0xfffffffe
    hexagon.registers.general[16] = 2
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0
    assert hexagon.registers.npc == pc + 4
