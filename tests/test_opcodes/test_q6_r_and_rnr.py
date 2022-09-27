def test_q6_r_and_rnr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x80\xf1')
    hexagon.registers.general[0] = 0x0000ffff
    hexagon.registers.general[1] = 0xff00ff00
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0xff000000
