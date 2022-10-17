from tests.test_opcodes.common import add_memory


def test_read_b_inc_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x00\x9b')
    add_memory(hexagon, b'\xf0\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffffff0
    assert hexagon.registers.general[0] == 0x40000021
