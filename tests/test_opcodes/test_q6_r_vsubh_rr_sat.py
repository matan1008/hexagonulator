import pytest


@pytest.mark.parametrize('rs, rt, rd, sat', [
    (0x80000001, 0x7f000002, 0x7fff0001, 1),
    (0x7f000001, 0x80000002, 0x80000001, 1),
    (0x00018000, 0x00027f00, 0x00017fff, 1),
    (0x00017f00, 0x00028000, 0x00018000, 1),
    (0x00010002, 0x00030004, 0x00020002, 0),
])
def test_q6_r_vsubh_rr_sat(hexagon, rs, rt, rd, sat):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\xa0\xf6')
    hexagon.registers.general[0] = rs
    hexagon.registers.general[1] = rt
    hexagon.cycle()
    assert hexagon.registers.general[2] == rd
    assert hexagon.registers.usr.ovf == sat
