from hexgonulator.common.bits_ops import bit_at, lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalZxth(Instruction):
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
            self.set_new_value_register(processor, self.d, lower_chunk(rs, 16))
        yield
