def test_sp3loop0_reg(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x18\xdf\xe0\x60')
    hexagon.registers.general[0] = 5
    hexagon.cycle()
    assert hexagon.registers.sa0 == pc - 4
    assert hexagon.registers.lc0 == 5
    assert hexagon.registers.usr.lpcfg == 3
    assert hexagon.registers.predicate[3] == 0


def test_sp3loop0_reg_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x01\x00\xc0\xe0\x60')
    hexagon.registers.general[0] = 5
    hexagon.cycle()
    assert hexagon.registers.sa0 == pc + 0x10000000
    assert hexagon.registers.lc0 == 5
    assert hexagon.registers.usr.lpcfg == 3
    assert hexagon.registers.predicate[3] == 0
