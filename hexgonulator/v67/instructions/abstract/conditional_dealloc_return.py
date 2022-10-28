from hexgonulator.common.bits_ops import bit_at
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalDeallocReturn(Instruction):
    def __init__(self, instr, s, d, pv, sense=True):
        super().__init__(instr)
        self.s = s
        self.d = d
        self.pv = pv
        self.sense = sense

    def execute(self, processor):
        ea = processor.registers.general[self.s]
        pv = processor.registers.predicate[self.pv]
        result = None
        yield
        if bit_at(pv, 0) == int(self.sense):
            tmp = processor.mem_get(ea, 8)
            result = processor.frame_unscramble(tmp)
        yield
        if result is not None:
            processor.registers.set_general_pair(self.d, result)
            processor.registers.sp = ea + 8
            processor.registers.pc = processor.registers.general[self.d + 1]
        yield
