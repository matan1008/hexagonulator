from tests.test_opcodes.common import add_memory


def test_deallocframe(hexagon):
    hexagon.registers.framekey = 0x00112233
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\x00\x90')
    add_memory(hexagon, b'\x00\x11\x22\x33\xff\x00\xff\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x00ee22cc
    assert hexagon.registers.sp == 0x40000028


def test_deallocframe_fp(hexagon):
    hexagon.registers.framekey = 0x00112233
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x1e\xc0\x1e\x90')
    add_memory(hexagon, b'\x00\x11\x22\x33\xff\x00\xff\x00', 0x40000020)
    hexagon.registers.fp = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.fp == 0x33221100
    assert hexagon.registers.lr == 0x00ee22cc
    assert hexagon.registers.sp == 0x40000028
