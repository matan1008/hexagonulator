from hexgonulator.common.bits_ops import to_unsigned, bit_at
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalCall(Instruction):
    def __init__(self, instr, r, pu, sense=True):
        super().__init__(instr)
        self.r = r
        self.pu = pu
        self.sense = sense

    def execute(self, processor):
        pu = processor.registers.predicate[self.pu]
        yield
        pc = to_unsigned(processor.registers.pc + self.r, 32)
        yield
        if bit_at(pu, 0) == int(self.sense):
            processor.registers.lr = processor.registers.npc
            processor.registers.pc = pc
        yield
