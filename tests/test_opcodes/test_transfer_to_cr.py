def test_transfer_to_cr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc0\x20\x62')
    hexagon.registers.general[0] = 2
    hexagon.cycle()
    assert hexagon.registers.sa0 == 2
