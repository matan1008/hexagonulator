def test_q6_r_combine_rlrh(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\xc0\xf3')
    hexagon.registers.general[0] = 0x3344aabb
    hexagon.registers.general[1] = 0x1122ccdd
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0xccdd3344
