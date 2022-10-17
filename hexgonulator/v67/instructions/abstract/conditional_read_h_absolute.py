from hexgonulator.common.bits_ops import bit_at, sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalReadHAbsolute(Instruction):
    def __init__(self, instr, d, pt, imm, sense=True, dot_new=False):
        super().__init__(instr)
        self.d = d
        self.pt = pt
        self.imm = imm
        self.sense = sense
        self.dot_new = dot_new

    def execute(self, processor):
        pt = processor.registers.predicate[self.pt]
        data = None
        yield
        if not self.dot_new and bit_at(pt, 0) == int(self.sense):
            data = processor.mem_get(self.imm, 2)
        yield
        if self.dot_new:
            pt = processor.registers.predicate[self.pt]
            if bit_at(pt, 0) == int(self.sense):
                data = processor.mem_get(self.imm, 2)
        if data is not None:
            processor.registers.general[self.d] = sign_extend(data, 16, 32)
        yield
