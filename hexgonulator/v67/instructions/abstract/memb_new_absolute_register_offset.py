from hexgonulator.common.bits_ops import lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class MembNewAbsoluteRegisterOffset(Instruction):
    def __init__(self, instr, u, t, shift, imm):
        super().__init__(instr)
        self.u = u
        self.t = t
        self.shift = shift
        self.imm = imm

    def execute(self, processor):
        ru = processor.registers.general[self.u]
        yield
        ea = self.imm + (ru << self.shift)
        yield
        nt = lower_chunk(processor.get_new_value_operand(self.t), 8)
        processor.mem_set(ea, 1, nt)
        yield
