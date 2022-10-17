from tests.test_opcodes.common import add_memory


def test_read_h_inc_reg(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\x40\x9d')
    add_memory(hexagon, b'\x00\xf0\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.m0.value = 0x20
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffff000
    assert hexagon.registers.general[0] == 0x40000040
