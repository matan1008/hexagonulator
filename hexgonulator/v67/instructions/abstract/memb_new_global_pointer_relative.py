from hexgonulator.common.bits_ops import lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class MembNewGlobalPointerRelative(Instruction):
    def __init__(self, instr, t, imm, use_gp=True):
        super().__init__(instr)
        self.t = t
        self.imm = imm
        self.use_gp = use_gp

    def execute(self, processor):
        gp = processor.registers.gp
        yield
        ea = (gp if self.use_gp else 0) + self.imm
        yield
        nt = lower_chunk(processor.get_new_value_operand(self.t), 8)
        processor.mem_set(ea, 1, nt)
        yield
