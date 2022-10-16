from hexgonulator.memory.controller import MemoryController
from hexgonulator.memory.ram import RAM


def test_conditional_read_b_reg_imm_not(hexagon):
    mem = RAM(8)
    mem.write(0, 4, b'\xf0\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x00\x45')
    hexagon.registers.general[0] = 0x4000001f
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffffff0


def test_conditional_read_b_reg_imm_not_false(hexagon):
    mem = RAM(8)
    mem.write(0, 4, b'\xf0\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x21\xc0\x00\x45')
    hexagon.registers.general[0] = 0x4000001f
    hexagon.registers.predicate[0] = 1
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0


def test_conditional_read_b_reg_imm_not_apply_extension(hexagon):
    mem = RAM(8)
    mem.write(0, 4, b'\xf0\x00\x00\x00')
    hexagon.memory.controllers.append(MemoryController(mem, start=0x40000020, end=0x40000024))
    hexagon.memory.controllers[0].mem.write(0, 8, b'\x00\x40\x00\x04\x21\xc0\x00\x45')
    hexagon.registers.general[0] = 0x1f
    hexagon.cycle()
    assert hexagon.registers.general[1] == 0xfffffff0
