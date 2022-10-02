def test_conditional_add_not_reg(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\x00\xfb')
    hexagon.registers.general[0] = 4
    hexagon.registers.general[1] = 3
    hexagon.registers.predicate[0] = 0
    hexagon.cycle()
    assert hexagon.registers.general[2] == 7


def test_conditional_add_not_reg_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\x00\xfb')
    hexagon.registers.general[0] = 4
    hexagon.registers.general[1] = 3
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0
