from tests.test_opcodes.common import add_memory


def test_membh_inc_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x20\x9a')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xffe0fff0
    assert hexagon.registers.general[0] == 0x40000022
