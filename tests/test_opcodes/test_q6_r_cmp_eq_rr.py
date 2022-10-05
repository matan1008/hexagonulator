import pytest


@pytest.mark.parametrize('rs, rt, rd', [
    (0xffffffff, 0xffffffff, 0xff),
    (0, 0xffffffff, 0),
    (0xffffffff, 0, 0),
])
def test_q6_r_cmp_eq_rr(hexagon, rs, rt, rd):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x40\xf3')
    hexagon.registers.general[0] = rs
    hexagon.registers.general[1] = rt
    hexagon.cycle()
    assert hexagon.registers.general[2] == rd
