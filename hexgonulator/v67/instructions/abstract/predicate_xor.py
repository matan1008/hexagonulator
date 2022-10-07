from hexgonulator.v67.instructions.instruction import Instruction


class PredicateXor(Instruction):
    def __init__(self, instr, d, s, t):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t

    def execute(self, processor):
        ps = processor.registers.predicate[self.s]
        pt = processor.registers.predicate[self.t]
        yield
        result = ps ^ pt
        yield
        processor.registers.predicate[self.d] = result
        yield
