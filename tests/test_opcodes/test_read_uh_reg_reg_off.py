from tests.test_opcodes.common import add_memory


def test_read_uh_reg_reg_off(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\x60\x3a')
    add_memory(hexagon, b'\x00\xf0\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0xf000
