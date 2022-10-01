def test_q6_r_aslh_r(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\x00\x70')
    hexagon.registers.general[0] = 0x0000f000
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xf0000000
