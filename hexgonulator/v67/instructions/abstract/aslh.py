from hexgonulator.common.bits_ops import lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class Aslh(Instruction):
    def __init__(self, instr, d, s):
        super().__init__(instr)
        self.d = d
        self.s = s

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        result = lower_chunk(rs, 16) << 16
        yield
        self.set_new_value_register(processor, self.d, result)
        yield
