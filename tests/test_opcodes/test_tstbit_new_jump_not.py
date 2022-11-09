def test_tstbit_new_jump_not(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x01\x40\x60\x70\xfe\xc0\xf2\x25')
    hexagon.registers.general[0] = 4
    hexagon.cycle()
    assert hexagon.registers.npc == pc - 4


def test_tstbit_new_jump_not_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x01\x40\x60\x70\xfe\xc0\xf2\x25')
    hexagon.registers.general[0] = 3
    hexagon.cycle()
    assert hexagon.registers.npc == pc + 8


def test_tstbit_new_jump_not_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 12, b'\x01\x40\x60\x70\x00\x40\x00\x01\x02\xc0\xc2\x25')
    hexagon.registers.general[0] = 4
    hexagon.cycle()
    assert hexagon.registers.npc == pc + 0x10000004
