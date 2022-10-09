def test_cmp_gt_and_jump_p0_imm_not_hint(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xe2\xf0\x10')
    hexagon.registers.general[0] = 3
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0xff
    assert hexagon.registers.npc == pc + 4


def test_cmp_gt_and_jump_p0_imm_not_hint_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xe2\xf0\x10')
    hexagon.registers.general[0] = 0xffffffff
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0
    assert hexagon.registers.npc == pc - 4
