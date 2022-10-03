from hexgonulator.common.bits_ops import bit_at
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalCombine(Instruction):
    def __init__(self, instr, dd, pu, s, t, sense=True, dot_new=False):
        super().__init__(instr)
        self.dd = dd
        self.pu = pu
        self.s = s
        self.t = t
        self.sense = sense
        self.dot_new = dot_new

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        pu = processor.registers.predicate[self.pu]
        yield
        yield
        if self.dot_new:
            pu = processor.registers.predicate[self.pu]
        if bit_at(pu, 0) == int(self.sense):
            processor.registers.general[self.dd] = rt
            processor.registers.general[self.dd + 1] = rs
        yield
