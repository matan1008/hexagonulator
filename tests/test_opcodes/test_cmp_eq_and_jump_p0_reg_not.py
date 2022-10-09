def test_cmp_eq_and_jump_p0_reg_not(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xc8\x70\x14')
    hexagon.registers.general[0] = 2
    hexagon.registers.general[16] = 2
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0xff
    assert hexagon.registers.npc == pc + 4


def test_cmp_eq_and_jump_p0_reg_not_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xc8\x70\x14')
    hexagon.registers.general[0] = 2
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0
    assert hexagon.registers.npc == pc - 4
