from tests.test_opcodes.common import add_memory


def test_memb_fifo_inc_reg_brev(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\x80\x9e')
    add_memory(hexagon, b'\x77\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000400
    hexagon.registers.general[1] = 0x221100ff
    hexagon.registers.general[2] = 0x66554433
    hexagon.registers.m0.value = 0x20
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x40000420
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
