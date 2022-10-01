def test_q6_r_mux_prr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\02\xc1\x00\xf4')
    hexagon.registers.general[0] = 4
    hexagon.registers.general[1] = 1
    hexagon.registers.predicate[0] = 0x1
    hexagon.cycle()
    assert hexagon.registers.general[2] == 4
