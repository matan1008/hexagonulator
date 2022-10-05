import pytest


@pytest.mark.parametrize('rs, rt, rd', [
    (0xffffffff, 0xffffffff, 0),
    (0, 0xffffffff, 0xff),
    (0xffffffff, 0, 0xff),
])
def test_q6_r_not_cmp_eq_rr(hexagon, rs, rt, rd):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x60\xf3')
    hexagon.registers.general[0] = rs
    hexagon.registers.general[1] = rt
    hexagon.cycle()
    assert hexagon.registers.general[2] == rd
