def test_transfer_from_cr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc0\x00\x6a')
    hexagon.registers.sa0 = 2
    hexagon.cycle()
    assert hexagon.registers.general[0] == 2
