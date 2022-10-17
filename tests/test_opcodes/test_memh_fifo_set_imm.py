from tests.test_opcodes.common import add_memory


def test_memh_fifo_set_imm(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x01\xd8\x40\x9a')
    add_memory(hexagon, b'\x66\x77\x00\x00', 0x20)
    hexagon.registers.general[1] = 0x1100ffff
    hexagon.registers.general[2] = 0x55443322
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x20
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544


def test_memh_fifo_set_imm_apply_extension(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x01\xd8\x40\x9a')
    add_memory(hexagon, b'\x66\x77\x00\x00', 0x40000020)
    hexagon.registers.general[1] = 0x1100ffff
    hexagon.registers.general[2] = 0x55443322
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x40000020
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
