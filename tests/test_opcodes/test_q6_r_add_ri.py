def test_q6_r_add_ri(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xe1\xc0\x00\xb0')
    hexagon.registers.general[0] = 3
    hexagon.cycle()
    assert hexagon.registers.general[1] == 10
