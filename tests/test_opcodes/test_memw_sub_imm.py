from tests.test_opcodes.common import add_memory


def test_memw_sub_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc4\x40\x3f')
    mem = add_memory(hexagon, b'\x00\x00\x00\x03', 0x40000020)
    hexagon.registers.general[0] = 0x40000000
    hexagon.cycle()
    assert mem.read(0, 4) == b'\xff\xff\xff\x02'


def test_memw_sub_imm_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x21\xc0\x40\x3f')
    mem = add_memory(hexagon, b'\x00\x00\x00\x03', 0x40000020)
    hexagon.registers.general[0] = 0x20
    hexagon.cycle()
    assert mem.read(0, 4) == b'\xff\xff\xff\x02'
