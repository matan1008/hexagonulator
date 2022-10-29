from tests.test_opcodes.common import add_memory


def test_membh_imm_reg_off(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x81\xd8\x20\x9c')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.general[0] = 0x20000000
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xffe0fff0


def test_membh_imm_reg_off_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x81\xd0\x20\x9c')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.general[0] = 0x10
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xffe0fff0
