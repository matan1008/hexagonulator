def test_q6_r_equals_i(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc0\xd8\x78')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xfffff000
