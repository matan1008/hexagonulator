from tests.test_opcodes.common import add_memory


def test_memubh_im_circ(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x60\x98')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.m0.length = 0x10
    hexagon.registers.cs0 = 0x40000020
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x00e000f0
    assert hexagon.registers.general[0] == 0x40000022


def test_memubh_im_circ_overflow(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x60\x98')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.m0.length = 0x12
    hexagon.registers.cs0 = 0x40000010
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x00e000f0
    assert hexagon.registers.general[0] == 0x40000010


def test_memubh_im_circ_underflow(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xe1\xc1\x60\x98')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.m0.length = 0x10
    hexagon.registers.cs0 = 0x40000020
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x00e000f0
    assert hexagon.registers.general[0] == 0x4000002e
