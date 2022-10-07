def test_add_to_pc(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x80\xd0\x49\x6a')
    hexagon.cycle()
    assert hexagon.registers.general[0] == pc + 33


def test_add_to_pc_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\x40\x00\x01\x00\xd0\x49\x6a')
    hexagon.cycle()
    assert hexagon.registers.general[0] == pc + 0x10000020
