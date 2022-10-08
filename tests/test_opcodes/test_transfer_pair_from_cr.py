def test_transfer_pair_from_cr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc0\x00\x68')
    hexagon.registers.sa0 = 2
    hexagon.registers.lc0 = 3
    hexagon.cycle()
    assert hexagon.registers.general[0] == 2
    assert hexagon.registers.general[1] == 3
