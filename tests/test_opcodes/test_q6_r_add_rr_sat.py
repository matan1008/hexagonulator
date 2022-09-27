import pytest


@pytest.mark.parametrize('rs, rt, rd, sat', [
    (0x7fffffff, 4, 0x7fffffff, 1),
    (0x7ffffff1, 4, 0x7ffffff5, 0),
])
def test_q6_r_add_ri_sat(hexagon, rs, rt, rd, sat):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x40\xf6')
    hexagon.registers.general[0] = rs
    hexagon.registers.general[1] = rt
    hexagon.cycle()
    assert hexagon.registers.general[2] == rd
    assert hexagon.registers.usr.ovf == sat
