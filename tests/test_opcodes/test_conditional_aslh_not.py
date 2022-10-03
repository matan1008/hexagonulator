def test_conditional_aslh_not(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xe8\x00\x70')
    hexagon.registers.general[0] = 0x0000f000
    hexagon.registers.predicate[0] = 0
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xf0000000


def test_conditional_aslh_not_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xe8\x00\x70')
    hexagon.registers.general[0] = 0x0000f000
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0
