from tests.test_opcodes.common import add_memory


def test_conditional_read_w_imm_not(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x80\xe8\x90\x9f')
    add_memory(hexagon, b'\x44\x33\x22\x11', 0x20)
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x11223344


def test_conditional_read_w_imm_not_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x80\xe8\x90\x9f')
    add_memory(hexagon, b'\x44\x33\x22\x11', 0x20)
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0


def test_conditional_read_w_imm_not_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x80\xe8\x90\x9f')
    add_memory(hexagon, b'\x44\x33\x22\x11', 0x40000020)
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x11223344
