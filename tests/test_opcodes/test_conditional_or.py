def test_conditional_or(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x20\xf9')
    hexagon.registers.general[0] = 0xffff0000
    hexagon.registers.general[1] = 0xff00ff00
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0xffffff00


def test_conditional_or_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x20\xf9')
    hexagon.registers.general[0] = 0xffff0000
    hexagon.registers.general[1] = 0xff00ff00
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0
