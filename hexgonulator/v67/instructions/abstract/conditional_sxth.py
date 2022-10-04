from hexgonulator.common.bits_ops import bit_at, sign_extend, lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalSxth(Instruction):
    def __init__(self, instr, d, pu, s, sense=True, dot_new=False):
        super().__init__(instr)
        self.d = d
        self.pu = pu
        self.s = s
        self.sense = sense
        self.dot_new = dot_new

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        pu = processor.registers.predicate[self.pu]
        yield
        yield
        if self.dot_new:
            pu = processor.registers.predicate[self.pu]
        if bit_at(pu, 0) == int(self.sense):
            processor.registers.general[self.d] = sign_extend(lower_chunk(rs, 16), 16, 32)
        yield
