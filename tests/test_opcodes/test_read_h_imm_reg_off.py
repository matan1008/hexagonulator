from tests.test_opcodes.common import add_memory


def test_read_h_imm_reg_off(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x81\xd8\x40\x9d')
    add_memory(hexagon, b'\x00\xf0\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x20000000
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffff000


def test_read_h_imm_reg_off_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x81\xd0\x40\x9d')
    add_memory(hexagon, b'\x00\xf0\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x10
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffff000
