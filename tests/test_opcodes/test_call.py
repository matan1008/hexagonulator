def test_call(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\xfe\xff\xff\x5b')
    hexagon.cycle()
    assert hexagon.registers.lr == pc + 4
    assert hexagon.registers.npc == pc - 4


def test_call_apply_extension(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x01\x00\xc0\x00\x5a')
    hexagon.cycle()
    assert hexagon.registers.lr == pc + 8
    assert hexagon.registers.npc == pc + 0x10000000
