def test_q6_r_equals_r(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\x60\x70')
    hexagon.registers.general[0] = 2
    hexagon.cycle()
    assert hexagon.registers.general[1] == 2
