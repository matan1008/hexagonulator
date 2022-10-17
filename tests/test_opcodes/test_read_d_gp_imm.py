from tests.test_opcodes.common import add_memory


def test_read_d_gp_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x80\xc0\xc0\x49')
    add_memory(hexagon, b'\x00\x11\x22\x33\x44\x55\x66\x77', 0x40000020)
    hexagon.registers.gp = 0x40000000
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x33221100
    assert hexagon.registers.general[1] == 0x77665544


def test_read_d_gp_imm_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x80\xc0\xc0\x49')
    add_memory(hexagon, b'\x00\x11\x22\x33\x44\x55\x66\x77', 0x40000020)
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x33221100
    assert hexagon.registers.general[1] == 0x77665544
