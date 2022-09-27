from hexgonulator.memory.hub import MemoryControllerHub
from .instructions.decoders.decode import decode_instruction
from .registers import Registers
from .sequencer import Sequencer
from .xunits import Xunits


class HexagonV67:
    def __init__(self):
        self.sequencer = Sequencer()
        self.registers = Registers()
        self.xunits = Xunits(self)
        self.memory = MemoryControllerHub()

    def mem_get(self, address, length):
        return self.memory[address, length]

    def cycle(self):
        packet = []
        for i in range(4):
            instruction_bytes = self.mem_get(self.registers.pc + (4 * i), 4)
            instr = decode_instruction(instruction_bytes)
            packet.append(instr)
            if instr.parse_field == 0b11:
                break
        self.xunits.set_instructions(self.sequencer.sequence(packet))
        self.xunits.cycle()
        self.registers.pc += 4 * len(packet)
