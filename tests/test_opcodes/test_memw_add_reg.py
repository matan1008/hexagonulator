from tests.test_opcodes.common import add_memory


def test_memw_add_reg(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc4\x40\x3e')
    mem = add_memory(hexagon, b'\x77\x30\x00\x01', 0x40000020)
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10000001
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x78\x30\x00\x11'


def test_memw_add_reg_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x01\xc0\x40\x3e')
    mem = add_memory(hexagon, b'\x77\x30\x00\x01', 0x40000020)
    hexagon.registers.general[0] = 0x20
    hexagon.registers.general[1] = 0x10000001
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x78\x30\x00\x11'
