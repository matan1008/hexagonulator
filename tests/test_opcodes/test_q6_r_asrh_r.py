def test_q6_r_asrh_r(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\x20\x70')
    hexagon.registers.general[0] = 0xf0000000
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffff000
