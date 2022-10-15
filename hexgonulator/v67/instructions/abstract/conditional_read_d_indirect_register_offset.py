from hexgonulator.common.bits_ops import lower_chunk, substring, bit_at
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalReadDIndirectRegisterOffset(Instruction):
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
            data = processor.mem_get(ea, 8)
        yield
        if self.dot_new:
            pv = processor.registers.predicate[self.pv]
            if bit_at(pv, 0) == int(self.sense):
                data = processor.mem_get(ea, 8)
        if data is not None:
            processor.registers.general[self.d] = lower_chunk(data, 32)
            processor.registers.general[self.d + 1] = substring(data, 63, 32)
        yield
