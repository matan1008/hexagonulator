from hexgonulator.common.bits_ops import bit_at
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalReadUbIndirectRegisterOffset(Instruction):
    def __init__(self, instr, d, s, t, pv, shift, sense=True, dot_new=False):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t
        self.pv = pv
        self.shift = shift
        self.sense = sense
        self.dot_new = dot_new

    def execute(self, processor):
        pv = processor.registers.predicate[self.pv]
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        data = None
        yield
        ea = rs + (rt << self.shift)
        if not self.dot_new and bit_at(pv, 0) == int(self.sense):
            data = processor.mem_get(ea, 1)
        yield
        if self.dot_new:
            pv = processor.registers.predicate[self.pv]
            if bit_at(pv, 0) == int(self.sense):
                data = processor.mem_get(ea, 1)
        if data is not None:
            self.set_new_value_register(processor, self.d, data)
        yield
