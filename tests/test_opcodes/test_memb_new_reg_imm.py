from tests.test_opcodes.common import add_memory


def test_memb_new_reg_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x03\x40\x62\x70\xfe\xe2\xa0\xa7')
    mem = add_memory(hexagon, b'\x00\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000022
    hexagon.registers.general[2] = 0x44332211
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x11\x00\x00\x00'


def test_memb_new_reg_imm_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 0xc, b'\x03\x40\x62\x70\x00\x40\x00\x04\x00\xc2\xa0\xa1')
    mem = add_memory(hexagon, b'\x00\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x20
    hexagon.registers.general[2] = 0x44332211
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x11\x00\x00\x00'
