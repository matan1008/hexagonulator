def test_q6_r_vavgh_rr_rnd(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x20\xf7')
    hexagon.registers.general[0] = 0x00030003
    hexagon.registers.general[1] = 0x00010002
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x00020003
