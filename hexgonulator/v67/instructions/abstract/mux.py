from hexgonulator.common.bits_ops import to_unsigned, bit_at
from hexgonulator.v67.instructions.instruction import Instruction


class Mux(Instruction):
    def __init__(self, instr, d, pu, reg_first=None, reg_second=None, imm_first=None, imm_second=None):
        super().__init__(instr)
        self.d = d
        self.pu = pu
        self.reg_first = reg_first
        self.reg_second = reg_second
        self.imm_first = imm_first
        self.imm_second = imm_second

    def execute(self, processor):
        first = processor.registers.general[self.reg_first] if self.reg_first is not None else self.imm_first
        second = processor.registers.general[self.reg_second] if self.reg_second is not None else self.imm_second
        pu = processor.registers.predicate[self.pu]
        yield
        result = to_unsigned(first if bit_at(pu, 0) else second, 32)
        yield
        processor.registers.general[self.d] = result
        yield
