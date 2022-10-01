from hexgonulator.common.bits_ops import lower_chunk, set_substring, substring
from hexgonulator.v67.instructions.instruction import Instruction


class Packhl(Instruction):
    def __init__(self, instr, dd, s, t):
        super().__init__(instr)
        self.dd = dd
        self.s = s
        self.t = t

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        yield
        low = set_substring(lower_chunk(rt, 16), 31, 16, lower_chunk(rs, 16))
        high = set_substring(substring(rt, 31, 16), 31, 16, substring(rs, 31, 16))
        yield
        processor.registers.general[self.dd] = low
        processor.registers.general[self.dd + 1] = high
        yield
