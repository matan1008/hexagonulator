def test_q6_r_equals_i(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc0\xd8\x78')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xfffff000


def test_q6_r_equals_i_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0c\x20\xc0\x00\x78')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xc0000001
