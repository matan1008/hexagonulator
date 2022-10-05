def test_q6_p_not_cmp_gt_ri(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xf0\xff\x60\x75')
    hexagon.registers.general[0] = 0
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0xff


def test_q6_p_not_cmp_gt_ri_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xf0\xff\x60\x75')
    hexagon.registers.general[0] = 0xffffffff
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0x00


def test_q6_p_not_cmp_gt_ri_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0f\xf0\xff\x60\x75')
    hexagon.registers.general[0] = 0xf000003f
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == 0
