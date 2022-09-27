def test_q6_r_sxtb_r(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\xa0\x70')
    hexagon.registers.general[0] = 0x000000f0
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffffff0
