def test_cmp_eq_and_jump_p1_imm_not_hint(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xe2\x70\x12')
    hexagon.registers.general[0] = 2
    hexagon.cycle()
    assert hexagon.registers.predicate[1] == 0xff
    assert hexagon.registers.npc == pc + 4


def test_cmp_eq_and_jump_p1_imm_not_hint_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xe2\x70\x12')
    hexagon.cycle()
    assert hexagon.registers.predicate[1] == 0
    assert hexagon.registers.npc == pc - 4