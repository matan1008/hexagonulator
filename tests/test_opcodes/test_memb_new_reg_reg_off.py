from tests.test_opcodes.common import add_memory


def test_memb_new_reg_reg_off(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x03\x40\x62\x70\x82\xc1\xa0\x3b')
    mem = add_memory(hexagon, b'\x00\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10
    hexagon.registers.general[2] = 0x44332211
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x11\x00\x00\x00'
