def test_conditional_sxth_not(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xe8\xe0\x70')
    hexagon.registers.general[0] = 0x0000f000
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffff000


def test_conditional_sxth_not_predicate_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xe8\xe0\x70')
    hexagon.registers.general[0] = 0x0000f000
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0
