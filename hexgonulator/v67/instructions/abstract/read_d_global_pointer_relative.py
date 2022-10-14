from hexgonulator.common.bits_ops import lower_chunk, substring
from hexgonulator.v67.instructions.instruction import Instruction


class ReadDGlobalPointerRelative(Instruction):
    def __init__(self, instr, d, imm, use_gp=True):
        super().__init__(instr)
        self.d = d
        self.imm = imm
        self.use_gp = use_gp

    def execute(self, processor):
        gp = processor.registers.gp
        yield
        ea = (gp if self.use_gp else 0) + self.imm
        data = processor.mem_get(ea, 8)
        yield
        processor.registers.general[self.d] = lower_chunk(data, 32)
        processor.registers.general[self.d + 1] = substring(data, 63, 32)
        yield
