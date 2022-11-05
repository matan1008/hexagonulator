from hexgonulator.common.bits_ops import sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class ReadBGlobalPointerRelative(Instruction):
    def __init__(self, instr, d, imm, use_gp=True):
        super().__init__(instr)
        self.d = d
        self.imm = imm
        self.use_gp = use_gp

    def execute(self, processor):
        gp = processor.registers.gp
        yield
        ea = (gp if self.use_gp else 0) + self.imm
        data = processor.mem_get(ea, 1)
        yield
        self.set_new_value_register(processor, self.d, sign_extend(data, 8, 32))
        yield
