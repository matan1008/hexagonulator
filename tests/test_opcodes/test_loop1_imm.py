def test_loop1_imm(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x3b\xdf\x20\x69')
    hexagon.cycle()
    assert hexagon.registers.sa1 == pc - 4
    assert hexagon.registers.lc1 == 7


def test_loop1_imm_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x01\x23\xc0\x20\x69')
    hexagon.cycle()
    assert hexagon.registers.sa1 == pc + 0x10000000
    assert hexagon.registers.lc1 == 7
