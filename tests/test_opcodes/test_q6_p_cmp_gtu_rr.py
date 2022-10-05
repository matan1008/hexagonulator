import pytest


@pytest.mark.parametrize('rs, rt, p0', [
    (0xffffffff, 0xffffffff, 0xff),
    (0, 0xffffffff, 0xff),
    (0xffffffff, 0, 0),
])
def test_q6_p_cmp_gtu_rr(hexagon, rs, rt, p0):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc1\x60\xf2')
    hexagon.registers.general[0] = rs
    hexagon.registers.general[1] = rt
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == p0
