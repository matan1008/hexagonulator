from .instructions.abstract.fastcorner9 import Fastcorner9

SLOT3_ICLASSES = (0b0001, 0b0010, 0b0101, 0b0110, 0b0111, 0b0101, 0b1000, 0b1011, 0b1100, 0b1101, 0b1110, 0b1111)
SLOT2_ICLASSES = (0b0001, 0b0010, 0b0101, 0b0111, 0b0101, 0b1000, 0b1011, 0b1100, 0b1101, 0b1110, 0b1111)
SLOT1_ICLASSES = (0b0011, 0b0100, 0b0111, 0b1001, 0b1011, 0b1111)
SLOT0_ICLASSES = (0b0011, 0b0100, 0b0111, 0b1001, 0b1010, 0b1011, 0b1111)

SLOTS_ICLASSES = (SLOT0_ICLASSES, SLOT1_ICLASSES, SLOT2_ICLASSES, SLOT3_ICLASSES)

SLOT2_EXCEPTIONS = (Fastcorner9,)
SLOTS_EXCEPTIONS = ((), (), SLOT2_EXCEPTIONS, ())


class Sequencer:
    def sequence(self, instructions: list):
        seq = [None, None, None, None]
        lowest_occupied = 4
        for instruction in instructions:
            if instruction.iclass == 0b0000:
                continue
            for slot in range(lowest_occupied - 1, -1, -1):
                if self.fits_slot(instruction, slot):
                    seq[slot] = instruction
                    lowest_occupied = slot
                    break
            else:
                raise Exception('Sequencing failure')
        return seq

    def fits_slot(self, instruction, slot):
        if instruction.iclass in SLOTS_ICLASSES[slot]:
            return True
        for exception in SLOTS_EXCEPTIONS[slot]:
            if isinstance(instruction, exception):
                return True
        return False
