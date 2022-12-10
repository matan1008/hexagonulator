from tests.test_opcodes.common import add_memory, set_predicate, HookedXunits


def test_conditional_memb_new_imm_new(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x03\x40\x62\x70\x80\xe2\xa2\xaf')
    mem = add_memory(hexagon, b'\x00\x00\x00\x00', 0x20)
    hexagon.registers.general[2] = 0x44332211
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x11\x00\x00\x00'


def test_conditional_memb_new_imm_new_false(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x03\x40\x62\x70\x80\xe2\xa2\xaf')
    mem = add_memory(hexagon, b'\x00\x00\x00\x00', 0x20)
    hexagon.registers.general[2] = 0x44332211
    hexagon.registers.predicate[0] = 1
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 0))
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x00\x00\x00\x00'


def test_conditional_memb_new_imm_new_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 12, b'\x03\x40\x62\x70\x00\x40\x00\x04\x80\xe2\xa2\xaf')
    mem = add_memory(hexagon, b'\x00\x00\x00\x00', 0x40000020)
    hexagon.registers.general[2] = 0x44332211
    hexagon.xunits = HookedXunits(hexagon, lambda: set_predicate(hexagon, 1))
    hexagon.cycle()
    assert mem.read(0, 4) == b'\x11\x00\x00\x00'
