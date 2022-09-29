def test_q6_r_vnavgh_rr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x60\xf7')
    hexagon.registers.general[0] = 0x00030001
    hexagon.registers.general[1] = 0x00070008
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x00020003
