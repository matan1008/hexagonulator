from hexgonulator.common.bits_ops import to_signed
from hexgonulator.v67.instructions.instruction import Instruction


class CmpEq(Instruction):
    def __init__(self, instr, pu, s, imm=None, t=None, sense=True):
        super().__init__(instr)
        self.pu = pu
        self.s = s
        self.imm = imm
        self.t = t
        self.sense = sense

    def execute(self, processor):
        rs = to_signed(processor.registers.general[self.s], 32)
        param2 = to_signed(processor.registers.general[self.t], 32) if self.t is not None else self.imm
        yield
        result = 0xff if (rs == param2) == self.sense else 0x00
        yield
        processor.registers.predicate[self.pu] = result
        yield
