def test_conditional_transfer_not(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc0\xdf\x8f\x7e')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xfffffffe


def test_conditional_transfer_not_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc0\xdf\x8f\x7e')
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0


def test_conditional_transfer_not_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x0f\xc0\xdf\x8f\x7e')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xf000003e
