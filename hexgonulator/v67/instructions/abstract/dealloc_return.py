from hexgonulator.v67.instructions.instruction import Instruction


class DeallocReturn(Instruction):
    def __init__(self, instr, s, d):
        super().__init__(instr)
        self.s = s
        self.d = d

    def execute(self, processor):
        ea = processor.registers.general[self.s]
        yield
        tmp = processor.mem_get(ea, 8)
        result = processor.frame_unscramble(tmp)
        yield
        processor.registers.set_general_pair(self.d, result)
        processor.registers.sp = ea + 8
        processor.registers.pc = processor.registers.general[self.d + 1]
        yield
