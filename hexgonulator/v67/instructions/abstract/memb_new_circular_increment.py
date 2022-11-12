from hexgonulator.common.bits_ops import to_signed, lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class MembNewCircularIncrement(Instruction):
    def __init__(self, instr, t, x, mu, imm=None):
        super().__init__(instr)
        self.t = t
        self.x = x
        self.imm = imm
        self.mu = mu

    def execute(self, processor):
        ea = processor.registers.general[self.x]
        yield
        m = processor.registers.m0 if self.mu == 0 else processor.registers.m1
        offset = self.imm if self.imm is not None else to_signed(m.i, 11)
        start_addr = processor.registers.cs0 if self.mu == 0 else processor.registers.cs1
        new_pointer = ((ea + offset - start_addr) % m.length) + start_addr
        yield
        processor.registers.general[self.x] = new_pointer
        nt = lower_chunk(processor.get_new_value_operand(self.t), 8)
        processor.mem_set(ea, 1, nt)
        yield
