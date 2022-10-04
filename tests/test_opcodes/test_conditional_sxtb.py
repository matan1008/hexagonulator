def test_conditional_sxtb(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xe0\xa0\x70')
    hexagon.registers.general[0] = 0x000000f0
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffffff0


def test_conditional_sxtb_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xe0\xa0\x70')
    hexagon.registers.general[0] = 0x000000f0
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0
