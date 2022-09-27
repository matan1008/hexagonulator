def test_q6_r_or_ri(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc1\xc0\x80\x76')
    hexagon.registers.general[0] = 0b101
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0b111
