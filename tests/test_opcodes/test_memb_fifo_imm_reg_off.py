from tests.test_opcodes.common import add_memory


def test_memb_fifo_imm_reg_off(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x81\xd8\x80\x9c')
    add_memory(hexagon, b'\x77\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x20000000
    hexagon.registers.general[1] = 0x221100ff
    hexagon.registers.general[2] = 0x66554433
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544


def test_memb_fifo_imm_reg_off_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x81\xd0\x80\x9c')
    add_memory(hexagon, b'\x77\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x10
    hexagon.registers.general[1] = 0x221100ff
    hexagon.registers.general[2] = 0x66554433
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
