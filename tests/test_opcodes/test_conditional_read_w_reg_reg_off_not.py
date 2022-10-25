from tests.test_opcodes.common import add_memory


def test_conditional_read_w_reg_reg_off_not(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\x80\x31')
    add_memory(hexagon, b'\x44\x33\x22\x11', 0x40000020)
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x11223344


def test_conditional_read_w_reg_reg_off_not_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x82\xc1\x80\x31')
    add_memory(hexagon, b'\x44\x33\x22\x11', 0x40000020)
    hexagon.registers.general[0] = 0x40000000
    hexagon.registers.general[1] = 0x10
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0
