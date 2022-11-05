from hexgonulator.common.bits_ops import to_unsigned, bit_at
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalAdd(Instruction):
    def __init__(self, instr, d, pu, s, sense=True, dot_new=False, t=None, imm=None):
        super().__init__(instr)
        self.d = d
        self.pu = pu
        self.s = s
        self.sense = sense
        self.dot_new = dot_new
        self.t = t
        self.imm = imm

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        addend = processor.registers.general[self.t] if self.t is not None else self.imm
        pu = processor.registers.predicate[self.pu]
        yield
        yield
        if self.dot_new:
            pu = processor.registers.predicate[self.pu]
        if bit_at(pu, 0) == int(self.sense):
            self.set_new_value_register(processor, self.d, to_unsigned(rs + addend, 32))
        yield
