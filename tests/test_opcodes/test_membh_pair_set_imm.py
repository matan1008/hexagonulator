from tests.test_opcodes.common import add_memory


def test_membh_pair_set_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xd8\xe0\x9a')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x20)
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x20
    assert hexagon.registers.general[1] == 0xffe0fff0
    assert hexagon.registers.general[2] == 0xfff00030


def test_membh_pair_set_imm_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x01\xd8\xe0\x9a')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x40000020
    assert hexagon.registers.general[1] == 0xffe0fff0
    assert hexagon.registers.general[2] == 0xfff00030
