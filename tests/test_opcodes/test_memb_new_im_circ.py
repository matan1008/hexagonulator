from tests.test_opcodes.common import add_memory


def test_memb_new_im_circ(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x03\x40\x62\x70\x08\xc2\xa0\xa9')
    mem = add_memory(hexagon, b'\x00\x00\x00\x00', 0x40000020)
    hexagon.registers.m0.length = 0x10
    hexagon.registers.cs0 = 0x40000020
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.general[2] = 0x44332211
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x40000021
    assert mem.read(0, 4) == b'\x11\x00\x00\x00'


def test_memb_new_im_circ_overflow(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x03\x40\x62\x70\x08\xc2\xa0\xa9')
    mem = add_memory(hexagon, b'\x00\x00\x00\x00', 0x40000020)
    hexagon.registers.m0.length = 0x11
    hexagon.registers.cs0 = 0x40000010
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.general[2] = 0x44332211
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x40000010
    assert mem.read(0, 4) == b'\x11\x00\x00\x00'


def test_memb_new_im_circ_underflow(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x03\x40\x62\x70\x78\xc2\xa0\xa9')
    mem = add_memory(hexagon, b'\x00\x00\x00\x00', 0x40000020)
    hexagon.registers.m0.length = 0x10
    hexagon.registers.cs0 = 0x40000020
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.general[2] = 0x44332211
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x4000002f
    assert mem.read(0, 4) == b'\x11\x00\x00\x00'
