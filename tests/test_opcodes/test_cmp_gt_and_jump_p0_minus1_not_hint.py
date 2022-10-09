def test_cmp_gt_and_jump_p0_minus1_not_hint(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xe1\xf0\x11')
    hexagon.registers.general[0] = 1
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0xff
    assert hexagon.registers.npc == pc + 4


def test_cmp_gt_and_jump_p0_minus1_not_hint_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xe1\xf0\x11')
    hexagon.registers.general[0] = 0xfffffffe
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0
    assert hexagon.registers.npc == pc - 4
