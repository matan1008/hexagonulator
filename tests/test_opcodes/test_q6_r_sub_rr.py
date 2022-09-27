def test_q6_r_sub_rr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x20\xf3')
    hexagon.registers.general[0] = 3
    hexagon.registers.general[1] = 7
    hexagon.cycle()
    assert hexagon.registers.general[2] == 4
