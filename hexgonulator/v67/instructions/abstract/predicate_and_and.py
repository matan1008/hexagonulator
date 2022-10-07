from hexgonulator.common.bits_ops import bit_not
from hexgonulator.v67.instructions.instruction import Instruction


class PredicateAndAnd(Instruction):
    def __init__(self, instr, d, s, t, u, neg=False):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t
        self.u = u
        self.neg = neg

    def execute(self, processor):
        ps = processor.registers.predicate[self.s]
        pt = processor.registers.predicate[self.t]
        pu = processor.registers.predicate[self.u]
        yield
        if self.neg:
            pu = bit_not(pu, 8)
        result = ps & (pt & pu)
        yield
        processor.registers.predicate[self.d] = result
        yield
