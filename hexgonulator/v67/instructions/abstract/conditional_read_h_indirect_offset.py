from hexgonulator.common.bits_ops import bit_at, sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalReadHIndirectOffset(Instruction):
    def __init__(self, instr, d, s, pt, imm, sense=True, dot_new=False):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.pt = pt
        self.imm = imm
        self.sense = sense
        self.dot_new = dot_new

    def execute(self, processor):
        pt = processor.registers.predicate[self.pt]
        rs = processor.registers.general[self.s]
        data = None
        yield
        ea = rs + self.imm
        if not self.dot_new and bit_at(pt, 0) == int(self.sense):
            data = processor.mem_get(ea, 2)
        yield
        if self.dot_new:
            pt = processor.registers.predicate[self.pt]
            if bit_at(pt, 0) == int(self.sense):
                data = processor.mem_get(ea, 2)
        if data is not None:
            self.set_new_value_register(processor, self.d, sign_extend(data, 16, 32))
        yield
