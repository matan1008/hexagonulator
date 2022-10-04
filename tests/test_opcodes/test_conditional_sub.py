def test_conditional_sub(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x20\xfb')
    hexagon.registers.general[0] = 5
    hexagon.registers.general[1] = 9
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[2] == 4


def test_conditional_sub_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x20\xfb')
    hexagon.registers.general[0] = 5
    hexagon.registers.general[1] = 9
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0
