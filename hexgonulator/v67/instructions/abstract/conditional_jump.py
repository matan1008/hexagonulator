from hexgonulator.common.bits_ops import to_unsigned, bit_at
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalJump(Instruction):
    def __init__(self, instr, r, pu, sense=True, hint=False, dot_new=False):
        super().__init__(instr)
        self.r = r
        self.pu = pu
        self.sense = sense
        self.hint = hint
        self.dot_new = dot_new

    def execute(self, processor):
        pu = processor.registers.predicate[self.pu]
        yield
        pc = to_unsigned(processor.registers.pc + self.r, 32)
        yield
        if self.dot_new:
            pu = processor.registers.predicate[self.pu]
        if bit_at(pu, 0) == int(self.sense):
            processor.registers.pc = pc
        yield
