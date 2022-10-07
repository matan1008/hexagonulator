def test_q6_p_and_and_ppp(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x83\xc1\x10\x6b')
    hexagon.registers.predicate[0] = 0b10101010
    hexagon.registers.predicate[1] = 0b01100110
    hexagon.registers.predicate[2] = 0b11110000
    hexagon.cycle()
    assert hexagon.registers.predicate[3] == 0b00100000
