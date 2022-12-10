from tests.test_opcodes.common import add_memory, set_predicate, HookedXunits


def test_conditional_memb_new_inc_imm_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x03\x40\x62\x70\xf8\xe2\xa0\xab')
    mem = add_memory(hexagon, b'\x00\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.general[2] = 0x44332211
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x11\x00\x00\x00'
    assert hexagon.registers.general[0] == 0x4000001f


def test_conditional_memb_new_inc_imm_new_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x03\x40\x62\x70\xf8\xe2\xa0\xab')
    mem = add_memory(hexagon, b'\x00\x00\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000020
    hexagon.registers.general[2] = 0x44332211
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x00\x00\x00\x00'
    assert hexagon.registers.general[0] == 0x40000020
