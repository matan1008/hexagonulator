from tests.test_opcodes.common import add_memory


def test_memb_fifo_inc_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x80\x9a')
    add_memory(hexagon, b'\x77\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.general[1] = 0x221100ff
    hexagon.registers.general[2] = 0x66554433
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x40000021
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
