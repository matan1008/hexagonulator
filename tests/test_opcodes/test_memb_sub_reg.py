from tests.test_opcodes.common import add_memory


def test_memb_sub_reg(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xd0\x00\x3e')
    mem = add_memory(hexagon, b'\x77\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x3
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x74\x00\x00\x00'


def test_memb_sub_reg_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x21\xc0\x00\x3e')
    mem = add_memory(hexagon, b'\x77\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x20
    hexagon.registers.general[1] = 0x3
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x74\x00\x00\x00'