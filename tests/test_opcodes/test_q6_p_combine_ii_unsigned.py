def test_q6_p_combine_ii_unsigned(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc0\xff\x9f\x7c')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x3f
    assert hexagon.registers.general[1] == 0xfffffffe


def test_q6_p_combine_ii_unsigned_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0f\xc0\xff\x9f\x7c')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xf000003f
    assert hexagon.registers.general[1] == 0xfffffffe
