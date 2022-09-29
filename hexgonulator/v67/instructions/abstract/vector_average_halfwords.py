from hexgonulator.common.bits_ops import to_signed, substring, lower_chunk, set_substring
from hexgonulator.v67.instructions.instruction import Instruction


class VectorAverageHalfwords(Instruction):
    def __init__(self, instr, d, s, t, round_=False, negative=False):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t
        self.round_ = round_
        self.negative = negative

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        yield
        rs_high = substring(rs, 31, 16)
        rs_low = lower_chunk(rs, 16)
        rt_high = substring(rt, 31, 16)
        rt_low = lower_chunk(rt, 16)
        if self.negative:
            result_low = (to_signed(rt_low, 16) - to_signed(rs_low, 16)) >> 1
            result_high = (to_signed(rt_high, 16) - to_signed(rs_high, 16)) >> 1
        else:
            result_low = (to_signed(rs_low, 16) + to_signed(rt_low, 16) + int(self.round_)) >> 1
            result_high = (to_signed(rs_high, 16) + to_signed(rt_high, 16) + int(self.round_)) >> 1

        result = set_substring(result_low, 31, 16, result_high)
        yield
        processor.registers.general[self.d] = result
        yield
