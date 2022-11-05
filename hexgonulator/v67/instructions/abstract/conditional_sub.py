from hexgonulator.common.bits_ops import bit_at, to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalSub(Instruction):
    def __init__(self, instr, d, pu, t, s, sense=True, dot_new=False):
        super().__init__(instr)
        self.d = d
        self.pu = pu
        self.s = s
        self.t = t
        self.dot_new = dot_new
        self.sense = sense

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        pu = processor.registers.predicate[self.pu]
        yield
        yield
        if self.dot_new:
            pu = processor.registers.predicate[self.pu]
        if bit_at(pu, 0) == int(self.sense):
            self.set_new_value_register(processor, self.d, to_unsigned(rt - rs, 32))
        yield
