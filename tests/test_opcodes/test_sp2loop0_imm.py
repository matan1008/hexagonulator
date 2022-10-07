def test_sp2loop0_imm(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x3b\xdf\xc0\x69')
    hexagon.cycle()
    assert hexagon.registers.sa0 == pc - 4
    assert hexagon.registers.lc0 == 7
    assert hexagon.registers.usr.lpcfg == 2
    assert hexagon.registers.predicate[3] == 0


def test_sp2loop0_imm_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x01\x23\xc0\xc0\x69')
    hexagon.cycle()
    assert hexagon.registers.sa0 == pc + 0x10000000
    assert hexagon.registers.lc0 == 7
    assert hexagon.registers.usr.lpcfg == 2
    assert hexagon.registers.predicate[3] == 0
