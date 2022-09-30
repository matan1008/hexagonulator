def test_q6_r_sub_ir(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc1\xc0\x40\x76')
    hexagon.registers.general[0] = 2
    hexagon.cycle()
    assert hexagon.registers.general[1] == 4


def test_q6_r_sub_ir_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0c\xc1\xc0\x40\x76')
    hexagon.registers.general[0] = 0x40000002
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x80000004
