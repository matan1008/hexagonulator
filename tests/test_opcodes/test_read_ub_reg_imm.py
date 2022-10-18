from tests.test_opcodes.common import add_memory


def test_read_ub_reg_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc1\xff\x20\x97')
    add_memory(hexagon, b'\xf0\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000022
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xf0


def test_read_ub_reg_imm_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x01\xc0\x20\x97')
    add_memory(hexagon, b'\xf0\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x20
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xf0
