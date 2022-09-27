def test_q6_r_xor_rr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x60\xf1')
    hexagon.registers.general[0] = 0xffff0000
    hexagon.registers.general[1] = 0xff00ff00
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x00ffff00
