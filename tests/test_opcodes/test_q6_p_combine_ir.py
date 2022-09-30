def test_q6_p_combine_ir(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xe2\xff\x20\x73')
    hexagon.registers.general[0] = 0x11223344
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x11223344
    assert hexagon.registers.general[3] == 0xffffffff


def test_q6_p_combine_ir_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0f\xe2\xff\x20\x73')
    hexagon.registers.general[0] = 0x11223344
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x11223344
    assert hexagon.registers.general[3] == 0xf000003f
