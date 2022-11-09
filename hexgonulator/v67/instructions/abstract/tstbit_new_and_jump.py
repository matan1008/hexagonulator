from hexgonulator.common.bits_ops import to_unsigned, to_signed
from hexgonulator.v67.instructions.instruction import Instruction


class TstbitNewAndJump(Instruction):
    def __init__(self, instr, r, s, sense=True, hint=False):
        super().__init__(instr)
        self.r = r
        self.s = s
        self.sense = sense
        self.hint = hint

    def execute(self, processor):
        yield
        yield
        ns = to_signed(processor.get_new_value_operand(self.s), 32)
        if (ns & 1) == self.sense:
            processor.registers.pc = to_unsigned(processor.registers.pc + self.r, 32)
        yield
