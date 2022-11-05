from hexgonulator.common.bits_ops import sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class ReadBIndirectWithRegisterOffset(Instruction):
    def __init__(self, instr, d, s, t, shift):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t
        self.shift = shift

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        yield
        ea = rs + (rt << self.shift)
        data = processor.mem_get(ea, 1)
        yield
        self.set_new_value_register(processor, self.d, sign_extend(data, 8, 32))
        yield
