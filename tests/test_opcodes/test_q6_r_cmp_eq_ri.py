def test_q6_r_cmp_eq_ri(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xe1\xff\x40\x73')
    hexagon.registers.general[0] = 0xffffffff
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xff


def test_q6_r_cmp_eq_ri_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xe1\xff\x40\x73')
    hexagon.registers.general[0] = 0
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0


def test_q6_r_cmp_eq_ri_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0f\xe1\xff\x40\x73')
    hexagon.registers.general[0] = 0xf000003f
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xff
