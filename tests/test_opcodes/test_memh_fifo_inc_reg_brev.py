from tests.test_opcodes.common import add_memory


def test_memh_fifo_inc_reg_brev(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xc0\x40\x9e')
    add_memory(hexagon, b'\x66\x77\x00\x00', 0x40000020)
    hexagon.registers.general[0] = 0x40000400
    hexagon.registers.general[1] = 0x1100ffff
    hexagon.registers.general[2] = 0x55443322
    hexagon.registers.m0.value = 0x20
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x40000420
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
