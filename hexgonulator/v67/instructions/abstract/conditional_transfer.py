from hexgonulator.common.bits_ops import to_unsigned, bit_at
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalTransfer(Instruction):
    def __init__(self, instr, d, pu, imm, sense=True, dot_new=False):
        super().__init__(instr)
        self.d = d
        self.pu = pu
        self.imm = imm
        self.sense = sense
        self.dot_new = dot_new

    def execute(self, processor):
        pu = processor.registers.predicate[self.pu]
        yield
        yield
        if self.dot_new:
            pu = processor.registers.predicate[self.pu]
        if bit_at(pu, 0) == int(self.sense):
            processor.registers.general[self.d] = to_unsigned(self.imm, 32)
        yield
