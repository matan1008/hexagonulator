def test_conditional_jump(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xe0\xdf\x5c')
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.lr == 0
    assert hexagon.registers.npc == pc - 4


def test_conditional_jump_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xe0\xdf\x5c')
    hexagon.cycle()
    assert hexagon.registers.lr == 0
    assert hexagon.registers.npc == pc + 4


def test_conditional_jump_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x01\x00\xc0\x00\x5c')
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.lr == 0
    assert hexagon.registers.npc == pc + 0x10000000
