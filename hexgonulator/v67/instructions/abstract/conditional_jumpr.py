from hexgonulator.common.bits_ops import bit_at
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalJumpr(Instruction):
    def __init__(self, instr, pu, s, sense=True, dot_new=False, direction_hint=False):
        super().__init__(instr)
        self.pu = pu
        self.s = s
        self.sense = sense
        self.dot_new = dot_new
        self.direction_hint = direction_hint

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        pu = processor.registers.predicate[self.pu]
        yield
        yield
        if self.dot_new:
            pu = processor.registers.predicate[self.pu]
        if bit_at(pu, 0) == int(self.sense):
            processor.registers.pc = rs
        yield
