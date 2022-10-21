from tests.test_opcodes.common import add_memory


def test_conditional_read_uh_imm_not(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x80\xe8\x70\x9f')
    add_memory(hexagon, b'\x00\xf0\x00\x00', 0x20)
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xf000


def test_conditional_read_uh_imm_not_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x80\xe8\x70\x9f')
    add_memory(hexagon, b'\x00\xf0\x00\x00', 0x20)
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0


def test_conditional_read_uh_imm_not_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x80\xe8\x70\x9f')
    add_memory(hexagon, b'\x00\xf0\x00\x00', 0x40000020)
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0xf000
