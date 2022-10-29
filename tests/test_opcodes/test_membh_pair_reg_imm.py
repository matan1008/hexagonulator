from tests.test_opcodes.common import add_memory


def test_membh_pair_reg_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xc1\xff\xe0\x96')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.general[0] = 0x40000028
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xffe0fff0
    assert hexagon.registers.general[2] == 0xfff00030


def test_membh_pair_pair_reg_imm_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x01\xc0\xe0\x96')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.general[0] = 0x20
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xffe0fff0
    assert hexagon.registers.general[2] == 0xfff00030
