def test_cmp_gt_and_jump_p1_minus1(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xc1\xb0\x13')
    hexagon.registers.general[0] = 1
    hexagon.cycle()
    assert hexagon.registers.predicate[1] == 0xff
    assert hexagon.registers.npc == pc - 4


def test_cmp_gt_and_jump_p1_minus1_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xc1\xb0\x13')
    hexagon.registers.general[0] = 0xfffffffe
    hexagon.cycle()
    assert hexagon.registers.predicate[1] == 0
    assert hexagon.registers.npc == pc + 4
