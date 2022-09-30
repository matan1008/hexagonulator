from hexgonulator.common.bits_ops import substring, lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class CombineHalfwords(Instruction):
    def __init__(self, instr, d, t, s, t_high, s_high):
        super().__init__(instr)
        self.d = d
        self.t = t
        self.s = s
        self.t_high = t_high
        self.s_high = s_high

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        yield
        high = substring(rt, 31, 16) if self.t_high else lower_chunk(rt, 16)
        low = substring(rs, 31, 16) if self.s_high else lower_chunk(rs, 16)
        result = (high << 16) | low
        yield
        processor.registers.general[self.d] = result
        yield
