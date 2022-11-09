from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class CmpGtuNewAndJump(Instruction):
    def __init__(self, instr, r, s, imm=None, t=None, sense=True, hint=False):
        super().__init__(instr)
        self.r = r
        self.s = s
        self.imm = imm
        self.t = t
        self.sense = sense
        self.hint = hint

    def execute(self, processor):
        param2 = processor.registers.general[self.t] if self.t is not None else self.imm
        yield
        yield
        ns = processor.get_new_value_operand(self.s)
        if (ns > param2) == self.sense:
            processor.registers.pc = to_unsigned(processor.registers.pc + self.r, 32)
        yield
