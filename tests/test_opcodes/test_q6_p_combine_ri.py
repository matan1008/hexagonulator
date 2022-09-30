def test_q6_p_combine_ri(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xe2\xff\x00\x73')
    hexagon.registers.general[0] = 0x11223344
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0xffffffff
    assert hexagon.registers.general[3] == 0x11223344


def test_q6_p_combine_ri_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0f\xe2\xff\x00\x73')
    hexagon.registers.general[0] = 0x11223344
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0xf000003f
    assert hexagon.registers.general[3] == 0x11223344
