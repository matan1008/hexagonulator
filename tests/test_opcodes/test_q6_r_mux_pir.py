def test_q6_r_mux_pir(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc1\xdf\x80\x73')
    hexagon.registers.predicate[0] = 0x1
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffffffe


def test_q6_r_mux_pir_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0f\xc1\xdf\x80\x73')
    hexagon.registers.predicate[0] = 0x1
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xf000003e
