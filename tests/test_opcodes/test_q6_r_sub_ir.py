def test_q6_r_sub_ir(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc1\xc0\x40\x76')
    hexagon.registers.general[0] = 2
    hexagon.cycle()
    assert hexagon.registers.general[1] == 4
