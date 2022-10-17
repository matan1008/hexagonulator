from tests.test_opcodes.common import add_memory


def test_memb_fifo_im_circ(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x80\x98')
    add_memory(hexagon, b'\x77\x00\x00\x00', 0x40000020)
    hexagon.registers.m0.length = 0x10
    hexagon.registers.cs0 = 0x40000020
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.general[1] = 0x221100ff
    hexagon.registers.general[2] = 0x66554433
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
    assert hexagon.registers.general[0] == 0x40000021


def test_memb_fifo_im_circ_overflow(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x80\x98')
    add_memory(hexagon, b'\x77\x00\x00\x00', 0x40000020)
    hexagon.registers.m0.length = 0x11
    hexagon.registers.cs0 = 0x40000010
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.general[1] = 0x221100ff
    hexagon.registers.general[2] = 0x66554433
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
    assert hexagon.registers.general[0] == 0x40000010


def test_memb_fifo_im_circ_underflow(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xe1\xc1\x80\x98')
    add_memory(hexagon, b'\x77\x00\x00\x00', 0x40000020)
    hexagon.registers.m0.length = 0x10
    hexagon.registers.cs0 = 0x40000020
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.general[1] = 0x221100ff
    hexagon.registers.general[2] = 0x66554433
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
    assert hexagon.registers.general[0] == 0x4000002f
