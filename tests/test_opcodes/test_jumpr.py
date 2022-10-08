def test_jumpr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc0\x80\x52')
    hexagon.registers.general[0] = 0x12345678
    hexagon.cycle()
    assert hexagon.registers.npc == 0x12345678
