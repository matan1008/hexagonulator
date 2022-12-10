from hexgonulator.common.bits_ops import bit_at, lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalMembNewIndirectRegisterOffset(Instruction):
    def __init__(self, instr, t, pv, s, u, shift, sense=True, dot_new=False):
        super().__init__(instr)
        self.t = t
        self.pv = pv
        self.s = s
        self.u = u
        self.shift = shift
        self.sense = sense
        self.dot_new = dot_new

    def execute(self, processor):
        pv = processor.registers.predicate[self.pv]
        rs = processor.registers.general[self.s]
        ru = processor.registers.general[self.u]
        predicate = False
        yield
        ea = rs + (ru << self.shift)
        if not self.dot_new:
            predicate = bit_at(pv, 0) == int(self.sense)
        yield
        if self.dot_new:
            pv = processor.registers.predicate[self.pv]
            predicate = bit_at(pv, 0) == int(self.sense)
        if predicate:
            nt = lower_chunk(processor.get_new_value_operand(self.t), 8)
            processor.mem_set(ea, 1, nt)
        yield
