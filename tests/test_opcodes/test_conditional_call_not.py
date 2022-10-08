def test_conditional_call_not(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xe0\xff\x5d')
    hexagon.cycle()
    assert hexagon.registers.lr == pc + 4
    assert hexagon.registers.npc == pc - 4


def test_conditional_call_not_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xe0\xff\x5d')
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.lr == 0
    assert hexagon.registers.npc == pc + 4


def test_conditional_call_not_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x01\x00\xc0\x20\x5d')
    hexagon.cycle()
    assert hexagon.registers.lr == pc + 8
    assert hexagon.registers.npc == pc + 0x10000000
