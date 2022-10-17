from tests.test_opcodes.common import add_memory


def test_memb_fifo_reg_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc1\xff\x80\x96')
    add_memory(hexagon, b'\x77\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000022
    hexagon.registers.general[1] = 0x221100ff
    hexagon.registers.general[2] = 0x66554433
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544


def test_memb_fifo_reg_imm_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x01\xc0\x80\x90')
    add_memory(hexagon, b'\x77\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x20
    hexagon.registers.general[1] = 0x221100ff
    hexagon.registers.general[2] = 0x66554433
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
