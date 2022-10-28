from tests.test_opcodes.common import add_memory, set_predicate, HookedXunits


def test_conditional_dealloc_return_new(hexagon):
    hexagon.registers.framekey = 0x00112233
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc8\x00\x96')
    add_memory(hexagon, b'\x00\x11\x22\x33\xff\x00\xff\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x00ee22cc
    assert hexagon.registers.sp == 0x40000028
    assert hexagon.registers.npc == 0x00ee22cc


def test_conditional_dealloc_return_new_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.registers.framekey = 0x00112233
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc8\x00\x96')
    add_memory(hexagon, b'\x00\x11\x22\x33\xff\x00\xff\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0
    assert hexagon.registers.general[2] == 0
    assert hexagon.registers.sp == 0
    assert hexagon.registers.npc == pc + 4
