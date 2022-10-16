from hexgonulator.common.bits_ops import to_signed
from hexgonulator.v67.instructions.instruction import Instruction


class ReadDCircularIncrement(Instruction):
    def __init__(self, instr, d, x, mu, imm=None):
        super().__init__(instr)
        self.d = d
        self.x = x
        self.imm = imm
        self.mu = mu

    def execute(self, processor):
        ea = processor.registers.general[self.x]
        yield
        m = processor.registers.m0 if self.mu == 0 else processor.registers.m1
        offset = self.imm if self.imm is not None else to_signed(m.i << 3, 14)
        start_addr = processor.registers.cs0 if self.mu == 0 else processor.registers.cs1
        new_pointer = ((ea + offset - start_addr) % m.length) + start_addr
        data = processor.mem_get(ea, 8)
        yield
        processor.registers.general[self.x] = new_pointer
        processor.registers.set_general_pair(self.d, data)
        yield
