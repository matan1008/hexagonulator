from hexgonulator.common.bits_ops import bit_at, to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class CmpGtuAndJump(Instruction):
    def __init__(self, instr, r, s, pu, imm=None, t=None, sense=True, hint=False):
        super().__init__(instr)
        self.r = r
        self.pu = pu
        self.s = s
        self.imm = imm
        self.t = t
        self.sense = sense
        self.hint = hint

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        param2 = processor.registers.general[self.t] if self.t is not None else self.imm
        yield
        result = 0xff if rs > param2 else 0x00
        pc = to_unsigned(processor.registers.pc + self.r, 32)
        yield
        processor.registers.predicate[self.pu] = result
        if bit_at(result, 0) == int(self.sense):
            processor.registers.pc = pc
        yield
