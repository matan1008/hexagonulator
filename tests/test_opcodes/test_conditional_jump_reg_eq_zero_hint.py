def test_conditional_jump_reg_eq_zero_hint(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xff\xa0\x61')
    hexagon.cycle()
    assert hexagon.registers.npc == pc - 4


def test_conditional_jump_reg_eq_zero_hint_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xff\xa0\x61')
    hexagon.registers.general[0] = 1
    hexagon.cycle()
    assert hexagon.registers.npc == pc + 4
