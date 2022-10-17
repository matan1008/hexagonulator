from hexgonulator.common.bits_ops import to_signed
from hexgonulator.v67.instructions.instruction import Instruction


class MemhFifoCircularIncrement(Instruction):
    def __init__(self, instr, y, x, mu, imm=None):
        super().__init__(instr)
        self.y = y
        self.x = x
        self.mu = mu
        self.imm = imm

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        ryy = processor.registers.get_general_pair(self.y)
        m = processor.registers.m0 if self.mu == 0 else processor.registers.m1
        yield
        offset = self.imm if self.imm is not None else to_signed(m.i << 1, 12)
        start_addr = processor.registers.cs0 if self.mu == 0 else processor.registers.cs1
        new_pointer = ((rx + offset - start_addr) % m.length) + start_addr
        tmp_v = processor.mem_get(rx, 2)
        ryy = (ryy >> 16) | (tmp_v << 48)
        yield
        processor.registers.general[self.x] = new_pointer
        processor.registers.set_general_pair(self.y, ryy)
        yield
