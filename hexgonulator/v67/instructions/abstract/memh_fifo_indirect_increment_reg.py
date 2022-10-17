from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class MemhFifoIndirectIncrementReg(Instruction):
    def __init__(self, instr, y, x, mu):
        super().__init__(instr)
        self.y = y
        self.x = x
        self.mu = mu

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        ryy = processor.registers.get_general_pair(self.y)
        m = processor.registers.m0 if self.mu == 0b0 else processor.registers.m1
        yield
        tmp_v = processor.mem_get(rx, 2)
        ryy = (ryy >> 16) | (tmp_v << 48)
        yield
        processor.registers.general[self.x] = to_unsigned(rx + m.value, 32)
        processor.registers.set_general_pair(self.y, ryy)
        yield
