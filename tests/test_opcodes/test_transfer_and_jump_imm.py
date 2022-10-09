def test_transfer_and_jump_imm(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xe0\x30\x16')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x20
    assert hexagon.registers.npc == pc - 4


def test_transfer_and_jump_imm_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x01\x00\xe0\x00\x16')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x20
    assert hexagon.registers.npc == pc + 0x10000000
