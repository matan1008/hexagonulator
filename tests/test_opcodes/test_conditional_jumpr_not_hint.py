def test_conditional_jumpr_not_hint(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xd0\x60\x53')
    hexagon.registers.general[0] = 0x12345678
    hexagon.cycle()
    assert hexagon.registers.npc == 0x12345678


def test_conditional_jumpr_not_hint_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xd0\x60\x53')
    hexagon.registers.general[0] = 0x12345678
    hexagon.registers.predicate[0] = 0xff
    hexagon.cycle()
    assert hexagon.registers.npc == pc + 4
