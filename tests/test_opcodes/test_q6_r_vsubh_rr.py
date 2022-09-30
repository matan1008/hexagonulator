def test_q6_r_vsubh_rr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x80\xf6')
    hexagon.registers.general[0] = 0x00030004
    hexagon.registers.general[1] = 0x000a0006
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x00070002
