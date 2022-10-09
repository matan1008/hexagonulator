def test_transfer_and_jump_reg(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xc1\x30\x17')
    hexagon.registers.general[0] = 0x12345678
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x12345678
    assert hexagon.registers.npc == pc - 4


def test_transfer_and_jump_reg_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x01\x00\xc1\x00\x17')
    hexagon.registers.general[0] = 0x12345678
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x12345678
    assert hexagon.registers.npc == pc + 0x10000000
