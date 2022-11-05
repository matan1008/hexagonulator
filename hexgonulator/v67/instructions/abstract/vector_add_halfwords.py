from hexgonulator.common.bits_ops import signed_sat_q, to_signed, substring, lower_chunk, unsigned_sat_q, \
    set_substring
from hexgonulator.v67.instructions.instruction import Instruction


class VectorAddHalfwords(Instruction):
    def __init__(self, instr, d, s, t, sat=False, signed=True):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t
        self.sat = sat
        self.signed = signed

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        yield
        rs_high = substring(rs, 31, 16)
        rs_low = lower_chunk(rs, 16)
        rt_high = substring(rt, 31, 16)
        rt_low = lower_chunk(rt, 16)
        saturated = False
        if self.signed:
            result_low = to_signed(rs_low, 16) + to_signed(rt_low, 16)
            result_high = to_signed(rs_high, 16) + to_signed(rt_high, 16)
            if self.sat:
                result_low, sat = signed_sat_q(result_low, 16)
                saturated |= sat
                result_high, sat = signed_sat_q(result_high, 16)
                saturated |= sat
        else:
            result_low = rs_low + rt_low
            result_high = rs_high + rt_high
            if self.sat:
                result_low, sat = unsigned_sat_q(result_low, 16)
                saturated |= sat
                result_high, sat = unsigned_sat_q(result_high, 16)
                saturated |= sat

        result = set_substring(result_low, 31, 16, result_high)
        yield
        self.set_new_value_register(processor, self.d, result)
        if self.sat and saturated:
            processor.registers.usr.ovf = 1
        yield
