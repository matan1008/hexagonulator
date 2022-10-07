from hexgonulator.common.bits_ops import bit_not
from hexgonulator.v67.instructions.instruction import Instruction


class PredicateNot(Instruction):
    def __init__(self, instr, d, s):
        super().__init__(instr)
        self.d = d
        self.s = s

    def execute(self, processor):
        ps = processor.registers.predicate[self.s]
        yield
        result = bit_not(ps, 8)
        yield
        processor.registers.predicate[self.d] = result
        yield
