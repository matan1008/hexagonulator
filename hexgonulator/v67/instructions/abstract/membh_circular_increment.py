from hexgonulator.common.bits_ops import to_signed, sign_extend, substring, set_substring
from hexgonulator.v67.instructions.instruction import Instruction


class MembhCircularIncrement(Instruction):
    def __init__(self, instr, d, x, mu, imm=None):
        super().__init__(instr)
        self.d = d
        self.x = x
        self.imm = imm
        self.mu = mu

    def execute(self, processor):
        ea = processor.registers.general[self.x]
        yield
        m = processor.registers.m0 if self.mu == 0 else processor.registers.m1
        offset = self.imm if self.imm is not None else to_signed(m.i << 1, 12)
        start_addr = processor.registers.cs0 if self.mu == 0 else processor.registers.cs1
        new_pointer = ((ea + offset - start_addr) % m.length) + start_addr
        data = processor.mem_get(ea, 2)
        result = 0
        for i in range(2):
            extended = sign_extend(substring(data, (i * 8) + 7, i * 8), 8, 16)
            result = set_substring(result, (i * 16) + 15, i * 16, extended)
        yield
        processor.registers.general[self.x] = new_pointer
        processor.registers.general[self.d] = result
        yield
