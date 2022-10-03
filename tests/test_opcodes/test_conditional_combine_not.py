def test_conditional_combine_not(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\x00\xfd')
    hexagon.registers.general[0] = 0x55667788
    hexagon.registers.general[1] = 0x11223344
    hexagon.registers.predicate[0] = 0
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x11223344
    assert hexagon.registers.general[3] == 0x55667788


def test_conditional_combine_not_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\x00\xfd')
    hexagon.registers.general[0] = 0x55667788
    hexagon.registers.general[1] = 0x11223344
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0
    assert hexagon.registers.general[3] == 0
