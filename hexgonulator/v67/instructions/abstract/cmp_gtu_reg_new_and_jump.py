from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class CmpGtuRegNewAndJump(Instruction):
    def __init__(self, instr, r, s, t, sense=True, hint=False):
        super().__init__(instr)
        self.r = r
        self.s = s
        self.t = t
        self.sense = sense
        self.hint = hint

    def execute(self, processor):
        rt = processor.registers.general[self.t]
        yield
        yield
        ns = processor.get_new_value_operand(self.s)
        if (rt > ns) == self.sense:
            processor.registers.pc = to_unsigned(processor.registers.pc + self.r, 32)
        yield
