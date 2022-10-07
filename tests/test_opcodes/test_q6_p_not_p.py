def test_q6_p_not_p(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\xc0\x6b')
    hexagon.registers.predicate[0] = 0b10101010
    hexagon.cycle()
    assert hexagon.registers.predicate[1] == 0b01010101
