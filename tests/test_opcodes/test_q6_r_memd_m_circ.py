from tests.test_opcodes.common import add_memory


def test_q6_r_memd_m_circ(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc2\xc0\x99')
    add_memory(hexagon, b'\x00\x11\x22\x33\x44\x55\x66\x77', 0x40000020)
    hexagon.registers.m0.i = 1
    hexagon.registers.m0.length = 0x10
    hexagon.registers.cs0 = 0x40000020
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
    assert hexagon.registers.general[0] == 0x40000028


def test_q6_r_memd_m_circ_overflow(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc2\xc0\x99')
    add_memory(hexagon, b'\x00\x11\x22\x33\x44\x55\x66\x77', 0x40000020)
    hexagon.registers.m0.i = 1
    hexagon.registers.m0.length = 0x18
    hexagon.registers.cs0 = 0x40000010
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
    assert hexagon.registers.general[0] == 0x40000010


def test_q6_r_memd_m_circ_underflow(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc2\xc0\x99')
    add_memory(hexagon, b'\x00\x11\x22\x33\x44\x55\x66\x77', 0x40000020)
    hexagon.registers.m0.i = 0b11111111111
    hexagon.registers.m0.length = 0x10
    hexagon.registers.cs0 = 0x40000020
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
    assert hexagon.registers.general[0] == 0x40000028
