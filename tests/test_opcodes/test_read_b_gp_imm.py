from tests.test_opcodes.common import add_memory


def test_read_b_gp_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc4\x00\x49')
    add_memory(hexagon, b'\xf0\x00\x00\x00', 0x40000020)
    hexagon.registers.gp = 0x40000000
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xfffffff0


def test_read_b_gp_imm_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x00\xc4\x00\x49')
    add_memory(hexagon, b'\xf0\x00\x00\x00', 0x40000020)
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xfffffff0
