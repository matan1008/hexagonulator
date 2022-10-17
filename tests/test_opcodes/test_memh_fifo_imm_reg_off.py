from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM


def test_memh_fifo_imm_reg_off(hexagon):
    mem = RAM(4)
    mem.write(0, 4, b'\x66\x77\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x81\xd8\x40\x9c')
    hexagon.registers.general[0] = 0x20000000
    hexagon.registers.general[1] = 0x1100ffff
    hexagon.registers.general[2] = 0x55443322
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544


def test_memh_fifo_imm_reg_off_apply_extension(hexagon):
    mem = RAM(4)
    mem.write(0, 4, b'\x66\x77\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x81\xd0\x40\x9c')
    hexagon.registers.general[0] = 0x10
    hexagon.registers.general[1] = 0x1100ffff
    hexagon.registers.general[2] = 0x55443322
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0x33221100
    assert hexagon.registers.general[2] == 0x77665544
