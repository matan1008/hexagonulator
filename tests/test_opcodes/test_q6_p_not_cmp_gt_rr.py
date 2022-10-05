import pytest


@pytest.mark.parametrize('rs, rt, p0', [
    (0xffffffff, 0xffffffff, 0),
    (0, 0xffffffff, 0xff),
    (0xffffffff, 0, 0),
])
def test_q6_p_not_cmp_gt_rr(hexagon, rs, rt, p0):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x10\xc1\x40\xf2')
    hexagon.registers.general[0] = rs
    hexagon.registers.general[1] = rt
    hexagon.cycle()
    assert hexagon.registers.predicate[0] == p0
