from tests.test_opcodes.common import add_memory


def test_memw_clrbit(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x50\xc4\x40\x3f')
    mem = add_memory(hexagon, b'\x77\x03\x03\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000000
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x77\x03\x02\x00'


def test_memw_clrbit_imm_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x50\xc0\x40\x3f')
    mem = add_memory(hexagon, b'\x77\x03\x03\x00', 0x40000020)
    hexagon.registers.general[0] = 0x20
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x77\x03\x02\x00'
