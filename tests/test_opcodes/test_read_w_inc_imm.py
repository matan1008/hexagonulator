from tests.test_opcodes.common import add_memory


def test_read_w_inc_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x80\x9b')
    add_memory(hexagon, b'\x44\x33\x22\x11', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x11223344
    assert hexagon.registers.general[0] == 0x40000024