from .instructions.abstract.all8 import All8
from .instructions.abstract.any8 import Any8
from .instructions.abstract.cmp_eq_and_jump import CmpEqAndJump
from .instructions.abstract.cmp_gt_and_jump import CmpGtAndJump
from .instructions.abstract.cmp_gtu_and_jump import CmpGtuAndJump
from .instructions.abstract.fastcorner9 import Fastcorner9
from .instructions.abstract.predicate_and import PredicateAnd
from .instructions.abstract.predicate_and_and import PredicateAndAnd
from .instructions.abstract.predicate_and_or import PredicateAndOr
from .instructions.abstract.predicate_not import PredicateNot
from .instructions.abstract.predicate_or import PredicateOr
from .instructions.abstract.predicate_or_and import PredicateOrAnd
from .instructions.abstract.predicate_or_or import PredicateOrOr
from .instructions.abstract.predicate_xor import PredicateXor
from .instructions.abstract.tstbit_and_jump import TstbitAndJump
from .instructions.concrete.conditional_jump import ConditionalJump
from .instructions.concrete.jump import Jump

SLOT3_ICLASSES = (0b0001, 0b0010, 0b0101, 0b0110, 0b0111, 0b0101, 0b1000, 0b1011, 0b1100, 0b1101, 0b1110, 0b1111)
SLOT2_ICLASSES = (0b0001, 0b0010, 0b0101, 0b0111, 0b0101, 0b1000, 0b1011, 0b1100, 0b1101, 0b1110, 0b1111)
SLOT1_ICLASSES = (0b0011, 0b0100, 0b0111, 0b1001, 0b1011, 0b1111)
SLOT0_ICLASSES = (0b0011, 0b0100, 0b0111, 0b1001, 0b1010, 0b1011, 0b1111)

SLOTS_ICLASSES = (SLOT0_ICLASSES, SLOT1_ICLASSES, SLOT2_ICLASSES, SLOT3_ICLASSES)

SLOT2_EXCEPTIONS = (
    Fastcorner9, All8, Any8, PredicateAnd, PredicateAndAnd, PredicateAndOr, PredicateNot, PredicateOr, PredicateOrAnd,
    PredicateOrOr, PredicateXor
)
SLOT1_EXCEPTIONS = (CmpEqAndJump, CmpGtAndJump, CmpGtuAndJump, TstbitAndJump, Jump, ConditionalJump)
SLOT0_EXCEPTIONS = (CmpEqAndJump, CmpGtAndJump, CmpGtuAndJump, TstbitAndJump, Jump, ConditionalJump)
SLOTS_EXCEPTIONS = (SLOT0_EXCEPTIONS, SLOT1_EXCEPTIONS, SLOT2_EXCEPTIONS, ())


class Sequencer:
    def __init__(self):
        self.sequenced = [None, None, None, None]

    def sequence(self, instructions: list):
        self.sequenced = [None, None, None, None]
        lowest_occupied = 4
        for instruction in instructions:
            if instruction.iclass == 0b0000:
                continue
            for slot in range(lowest_occupied - 1, -1, -1):
                if self.fits_slot(instruction, slot):
                    self.sequenced[slot] = instruction
                    lowest_occupied = slot
                    break
            else:
                raise Exception('Sequencing failure')
        return self.sequenced

    def fits_slot(self, instruction, slot):
        if instruction.iclass in SLOTS_ICLASSES[slot]:
            return True
        for exception in SLOTS_EXCEPTIONS[slot]:
            if isinstance(instruction, exception):
                return True
        return False
