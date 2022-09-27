def test_q6_r_add_rr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x00\xf3')
    hexagon.registers.general[0] = 3
    hexagon.registers.general[1] = 4
    hexagon.cycle()
    assert hexagon.registers.general[2] == 7
