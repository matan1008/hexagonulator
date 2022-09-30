def test_q6_r_or_ri(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc1\xc0\x80\x76')
    hexagon.registers.general[0] = 0b101
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0b111


def test_q6_r_or_ri_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0c\xc1\xc0\x80\x76')
    hexagon.registers.general[0] = 0x50000005
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xd0000007
