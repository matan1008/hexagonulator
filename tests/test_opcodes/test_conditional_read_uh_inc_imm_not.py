from tests.test_opcodes.common import add_memory


def test_conditional_read_uh_inc_imm_not(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xe1\xe9\x60\x9b')
    add_memory(hexagon, b'\x00\xf0\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xf000
    assert hexagon.registers.general[0] == 0x4000001e


def test_conditional_read_uh_inc_imm_not_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xe1\xe9\x60\x9b')
    add_memory(hexagon, b'\x00\xf0\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0
    assert hexagon.registers.general[0] == 0x40000020
