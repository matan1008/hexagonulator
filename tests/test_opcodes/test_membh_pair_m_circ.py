from tests.test_opcodes.common import add_memory


def test_membh_pair_m_circ(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc2\xe0\x98')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.m0.i = 1
    hexagon.registers.m0.length = 0x10
    hexagon.registers.cs0 = 0x40000020
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xffe0fff0
    assert hexagon.registers.general[2] == 0xfff00030
    assert hexagon.registers.general[0] == 0x40000024


def test_membh_pair_m_circ_overflow(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc2\xe0\x98')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.m0.i = 1
    hexagon.registers.m0.length = 0x14
    hexagon.registers.cs0 = 0x40000010
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xffe0fff0
    assert hexagon.registers.general[2] == 0xfff00030
    assert hexagon.registers.general[0] == 0x40000010


def test_membh_pair_m_circ_underflow(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc2\xe0\x98')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.m0.i = 0b11111111111
    hexagon.registers.m0.length = 0x10
    hexagon.registers.cs0 = 0x40000020
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xffe0fff0
    assert hexagon.registers.general[2] == 0xfff00030
    assert hexagon.registers.general[0] == 0x4000002c
