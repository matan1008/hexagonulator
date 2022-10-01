def test_q6_r_mux_pii(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc0\xff\x7f\x7a')
    hexagon.registers.predicate[0] = 0x1
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xfffffffe


def test_q6_r_mux_pii_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0f\xc0\xff\x7f\x7a')
    hexagon.registers.predicate[0] = 0x1
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xf000003e
