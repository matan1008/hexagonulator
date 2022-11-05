from hexgonulator.v67.instructions.instruction import Instruction


class TransferFromCr(Instruction):
    def __init__(self, instr, d, s):
        super().__init__(instr)
        self.d = d
        self.s = s

    def execute(self, processor):
        cs = processor.registers.transfer_read_control_register(self.s)
        yield
        yield
        self.set_new_value_register(processor, self.d, cs)
        yield
