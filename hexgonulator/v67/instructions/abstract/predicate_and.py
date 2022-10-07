from hexgonulator.common.bits_ops import bit_not
from hexgonulator.v67.instructions.instruction import Instruction


class PredicateAnd(Instruction):
    def __init__(self, instr, d, s, t, neg=False):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t
        self.neg = neg

    def execute(self, processor):
        ps = processor.registers.predicate[self.s]
        pt = processor.registers.predicate[self.t]
        yield
        if self.neg:
            ps = bit_not(ps, 8)
        result = pt & ps
        yield
        processor.registers.predicate[self.d] = result
        yield
