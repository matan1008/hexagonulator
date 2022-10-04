from hexgonulator.common.bits_ops import substring, chain
from ..abstract.conditional_transfer import ConditionalTransfer


class ConditionalTransferNot(ConditionalTransfer):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        u2 = substring(instr, 22, 21)
        imm_high = substring(instr, 19, 16)
        imm_low = substring(instr, 12, 5)
        imm = apply_extension(chain(imm_high, imm_low, 8), 12, signed=True)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, pu=u2, imm=imm, sense=False)

    def __repr__(self):
        return f'if (!P{self.pu}) R{self.d}=#{self.imm}'
