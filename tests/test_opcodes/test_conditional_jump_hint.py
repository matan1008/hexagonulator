def test_conditional_jump_hint(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xf0\xdf\x5c')
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.lr == 0
    assert hexagon.registers.npc == pc - 4


def test_conditional_jump_hint_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xf0\xdf\x5c')
    hexagon.cycle()
    assert hexagon.registers.lr == 0
    assert hexagon.registers.npc == pc + 4


def test_conditional_jump_hint_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x01\x00\xd0\x00\x5c')
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.lr == 0
    assert hexagon.registers.npc == pc + 0x10000000
