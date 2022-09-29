import pytest


@pytest.mark.parametrize('rs, rt, rd, sat', [
    (0x7f000001, 0x7f000002, 0xfe000003, 0),
    (0x81000001, 0x81000002, 0xffff0003, 1),
    (0x00017f00, 0x00027f00, 0x0003fe00, 0),
    (0x00018100, 0x00028100, 0x0003ffff, 1),
    (0x00010002, 0x00030004, 0x00040006, 0),
])
def test_q6_r_vadduh_rr_sat(hexagon, rs, rt, rd, sat):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x60\xf6')
    hexagon.registers.general[0] = rs
    hexagon.registers.general[1] = rt
    hexagon.cycle()
    assert hexagon.registers.general[2] == rd
    assert hexagon.registers.usr.ovf == sat
