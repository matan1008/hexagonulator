import pytest


@pytest.mark.parametrize('ps, pd', [
    (0b00000000, 0x00),
    (0b00000001, 0x0),
    (0b1000000, 0x0),
    (0b11111111, 0xff),
])
def test_q6_p_all8_p(hexagon, ps, pd):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\xa0\x6b')
    hexagon.registers.predicate[0] = ps
    hexagon.cycle()
    assert hexagon.registers.predicate[1] == pd
