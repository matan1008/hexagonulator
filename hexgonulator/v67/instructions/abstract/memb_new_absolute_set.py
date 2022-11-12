from hexgonulator.common.bits_ops import lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class MembNewAbsoluteSet(Instruction):
    def __init__(self, instr, t, e, imm):
        super().__init__(instr)
        self.t = t
        self.e = e
        self.imm = imm

    def execute(self, processor):
        yield
        yield
        nt = lower_chunk(processor.get_new_value_operand(self.t), 8)
        processor.mem_set(self.imm, 1, nt)
        processor.registers.general[self.e] = self.imm
        yield
