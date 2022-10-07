import pytest


@pytest.mark.parametrize('ps, pt, pd', [
    (0b00000001, 0b00000001, 0xff),
    (0b00000001, 0b11111111, 0x0),
    (0b11111111, 0b10000000, 0x0),
    (0b00011111, 0b11110000, 0x0),
    (0b11111000, 0b00001111, 0x0),
])
def test_q6_p_fastcorner9_pp(hexagon, ps, pt, pd):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x92\xe1\x00\x6b')
    hexagon.registers.predicate[0] = ps
    hexagon.registers.predicate[1] = pt
    hexagon.cycle()
    assert hexagon.registers.predicate[2] == pd
