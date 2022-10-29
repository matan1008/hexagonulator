from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class MemhAddReg(Instruction):
    def __init__(self, instr, s, offset, t):
        super().__init__(instr)
        self.s = s
        self.offset = offset
        self.t = t

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        yield
        ea = rs + self.offset
        tmp = processor.mem_get(ea, 2)
        tmp += rt
        processor.mem_set(ea, 2, to_unsigned(tmp, 16))
        yield
        yield
