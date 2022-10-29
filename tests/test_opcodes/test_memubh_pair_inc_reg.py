from tests.test_opcodes.common import add_memory


def test_memubh_pair_inc_reg(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\xa0\x9c')
    add_memory(hexagon, b'\xf0\xe0\x30\xf0', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.m0.value = 0x20
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x00e000f0
    assert hexagon.registers.general[2] == 0x00f00030
    assert hexagon.registers.general[0] == 0x40000040
