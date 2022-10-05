def test_q6_p_cmp_gtu_ri(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xe0\xff\x80\x75')
    hexagon.registers.general[0] = 0x1ff
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0xff


def test_q6_p_cmp_gtu_ri_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xe0\xff\x80\x75')
    hexagon.registers.general[0] = 0x200
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0x00


def test_q6_p_cmp_gtu_ri_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0f\xe0\xff\x80\x75')
    hexagon.registers.general[0] = 0xf000003f
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0xff
