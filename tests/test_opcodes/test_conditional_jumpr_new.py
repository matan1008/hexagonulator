from tests.test_opcodes.common import set_predicate, HookedXunits


def test_conditional_jumpr_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc8\x40\x53')
    hexagon.registers.general[0] = 0x12345678
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert hexagon.registers.npc == 0x12345678


def test_conditional_jumpr_new_false(hexagon):
    pc = hexagon.registers.pc
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc8\x40\x53')
    hexagon.registers.general[0] = 0x12345678
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert hexagon.registers.npc == pc + 4
