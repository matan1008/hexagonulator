from tests.test_opcodes.common import add_memory


def test_read_d_inc_reg_brev(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\xc0\x9f')
    add_memory(hexagon, b'\x00\x11\x22\x33\x44\x55\x66\x77', 0x40000020)
    hexagon.registers.general[0] = 0x40000400
    hexagon.registers.m0.value = 0x20
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
    assert hexagon.registers.general[0] == 0x40000420
