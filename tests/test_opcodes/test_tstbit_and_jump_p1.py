def test_tstbit_and_jump_p1(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xc3\xb0\x13')
    hexagon.registers.general[0] = 5
    hexagon.cycle()
    assert hexagon.registers.predicate[1] == 0xff
    assert hexagon.registers.npc == pc - 4


def test_tstbit_and_jump_p1_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xc3\xb0\x13')
    hexagon.registers.general[0] = 4
    hexagon.cycle()
    assert hexagon.registers.predicate[1] == 0
    assert hexagon.registers.npc == pc + 4
