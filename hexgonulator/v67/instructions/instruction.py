from abc import abstractmethod, ABC

from hexgonulator.common.bits_ops import substring


class Instruction(ABC):
    def __init__(self, instr):
        self.instr = instr

    @classmethod
    def from_int(cls, instr):
        pass

    @property
    def iclass(self):
        return substring(self.instr, 31, 28)

    @property
    def parse_field(self):
        return substring(self.instr, 15, 14)

    @abstractmethod
    def execute(self, processor):
        """
        Execute the opcode on the given processor
        :param processor: Processor to run opcode on.
        """
        pass
