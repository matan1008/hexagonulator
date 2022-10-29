from tests.test_opcodes.common import add_memory


def test_memw_or_reg(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x61\xc4\x40\x3e')
    mem = add_memory(hexagon, b'\x77\x11\x00\x20', 0x40000020)
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10002008
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x7f\x31\x00\x30'


def test_memw_or_reg_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x61\xc0\x40\x3e')
    mem = add_memory(hexagon, b'\x77\x11\x00\x20', 0x40000020)
    hexagon.registers.general[0] = 0x20
    hexagon.registers.general[1] = 0x10002008
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x7f\x31\x00\x30'
