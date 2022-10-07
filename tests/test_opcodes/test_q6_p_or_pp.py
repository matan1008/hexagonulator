def test_q6_p_or_pp(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x20\x6b')
    hexagon.registers.predicate[0] = 0b10101010
    hexagon.registers.predicate[1] = 0b01100110
    hexagon.cycle()
    assert hexagon.registers.predicate[2] == 0b11101110
