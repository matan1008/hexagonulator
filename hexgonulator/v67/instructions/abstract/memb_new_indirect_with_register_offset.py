from hexgonulator.common.bits_ops import lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class MembNewIndirectWithRegisterOffset(Instruction):
    def __init__(self, instr, s, u, t, shift):
        super().__init__(instr)
        self.s = s
        self.u = u
        self.t = t
        self.shift = shift

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        ru = processor.registers.general[self.u]
        yield
        ea = rs + (ru << self.shift)
        yield
        nt = lower_chunk(processor.get_new_value_operand(self.t), 8)
        processor.mem_set(ea, 1, nt)
        yield
