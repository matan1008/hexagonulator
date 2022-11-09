from hexgonulator.common.bits_ops import to_unsigned, to_signed
from hexgonulator.v67.instructions.instruction import Instruction


class CmpGtRegNewAndJump(Instruction):
    def __init__(self, instr, r, s, t, sense=True, hint=False):
        super().__init__(instr)
        self.r = r
        self.s = s
        self.t = t
        self.sense = sense
        self.hint = hint

    def execute(self, processor):
        rt = to_signed(processor.registers.general[self.t], 32)
        yield
        yield
        ns = to_signed(processor.get_new_value_operand(self.s), 32)
        if (rt > ns) == self.sense:
            processor.registers.pc = to_unsigned(processor.registers.pc + self.r, 32)
        yield
