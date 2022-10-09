def test_cmp_gtu_and_jump_p1_imm(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xc2\x30\x13')
    hexagon.registers.general[0] = 3
    hexagon.cycle()
    assert hexagon.registers.predicate[1] == 0xff
    assert hexagon.registers.npc == pc - 4


def test_cmp_gtu_and_jump_p1_imm_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xc2\x30\x13')
    hexagon.cycle()
    assert hexagon.registers.predicate[1] == 0
    assert hexagon.registers.npc == pc + 4
