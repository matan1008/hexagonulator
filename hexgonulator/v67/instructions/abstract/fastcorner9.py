from hexgonulator.common.bits_ops import set_substring
from hexgonulator.v67.instructions.instruction import Instruction


class Fastcorner9(Instruction):
    def __init__(self, instr, pd, ps, pt, sense=True):
        super().__init__(instr)
        self.pd = pd
        self.ps = ps
        self.pt = pt
        self.sense = sense

    def execute(self, processor):
        ps = processor.registers.predicate[self.ps]
        pt = processor.registers.predicate[self.pt]
        yield
        half = (ps << 8) | pt
        tmp = set_substring(half, 31, 16, half)
        for _ in range(8):
            tmp &= tmp >> 1
        result = 0xff if (tmp == 0) == self.sense else 0x00
        yield
        processor.registers.predicate[self.pd] = result
        yield
