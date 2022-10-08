def test_callr(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc0\xa0\x50')
    hexagon.registers.general[0] = 0x12345678
    hexagon.cycle()
    assert hexagon.registers.lr == pc + 4
    assert hexagon.registers.npc == 0x12345678
