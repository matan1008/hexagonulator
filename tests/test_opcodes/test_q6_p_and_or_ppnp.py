def test_q6_p_and_or_ppnp(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x83\xc1\xb0\x6b')
    hexagon.registers.predicate[0] = 0b10101010
    hexagon.registers.predicate[1] = 0b01100110
    hexagon.registers.predicate[2] = 0b11110000
    hexagon.cycle()
    assert hexagon.registers.predicate[3] == 0b00101010
