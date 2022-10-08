def test_transfer_pair_to_cr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc0\x20\x63')
    hexagon.registers.general[0] = 2
    hexagon.registers.general[1] = 3
    hexagon.cycle()
    assert hexagon.registers.sa0 == 2
    assert hexagon.registers.lc0 == 3
