from hexgonulator.common.bits_ops import bit_at
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalCallr(Instruction):
    def __init__(self, instr, s, pu, sense=True):
        super().__init__(instr)
        self.s = s
        self.pu = pu
        self.sense = sense

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        pu = processor.registers.predicate[self.pu]
        yield
        yield
        if bit_at(pu, 0) == int(self.sense):
            processor.registers.lr = processor.registers.npc
            processor.registers.pc = rs
        yield
