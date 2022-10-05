def test_conditional_zxth(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xe0\xc0\x70')
    hexagon.registers.general[0] = 0x11223344
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x3344


def test_conditional_zxth_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xe0\xc0\x70')
    hexagon.registers.general[0] = 0x11223344
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0
