from hexgonulator.common.bits_ops import substring, bit_at
from hexgonulator.v67.instructions.concrete.add_to_pc import AddToPc
from hexgonulator.v67.instructions.concrete.loop0_imm import Loop0Imm
from hexgonulator.v67.instructions.concrete.loop0_reg import Loop0Reg
from hexgonulator.v67.instructions.concrete.loop1_imm import Loop1Imm
from hexgonulator.v67.instructions.concrete.loop1_reg import Loop1Reg
from hexgonulator.v67.instructions.concrete.q6_p_all8_p import Q6PAll8P
from hexgonulator.v67.instructions.concrete.q6_p_and_and_ppnp import Q6PAndAndPpnp
from hexgonulator.v67.instructions.concrete.q6_p_and_and_ppp import Q6PAndAndPpp
from hexgonulator.v67.instructions.concrete.q6_p_and_or_ppnp import Q6PAndOrPpnp
from hexgonulator.v67.instructions.concrete.q6_p_and_or_ppp import Q6PAndOrPpp
from hexgonulator.v67.instructions.concrete.q6_p_and_pnp import Q6PAndPnp
from hexgonulator.v67.instructions.concrete.q6_p_and_pp import Q6PAndPp
from hexgonulator.v67.instructions.concrete.q6_p_any8_p import Q6PAny8P
from hexgonulator.v67.instructions.concrete.q6_p_fastcorner9_pp import Q6PFastcorner9Pp
from hexgonulator.v67.instructions.concrete.q6_p_not_fastcorner9_pp import Q6PNotFastcorner9Pp
from hexgonulator.v67.instructions.concrete.q6_p_not_p import Q6PNotP
from hexgonulator.v67.instructions.concrete.q6_p_or_and_ppnp import Q6POrAndPpnp
from hexgonulator.v67.instructions.concrete.q6_p_or_and_ppp import Q6POrAndPpp
from hexgonulator.v67.instructions.concrete.q6_p_or_or_ppnp import Q6POrOrPpnp
from hexgonulator.v67.instructions.concrete.q6_p_or_or_ppp import Q6POrOrPpp
from hexgonulator.v67.instructions.concrete.q6_p_or_pnp import Q6POrPnp
from hexgonulator.v67.instructions.concrete.q6_p_or_pp import Q6POrPp
from hexgonulator.v67.instructions.concrete.q6_p_xor_pp import Q6PXorPp
from hexgonulator.v67.instructions.concrete.sp1loop0_imm import Sp1Loop0Imm
from hexgonulator.v67.instructions.concrete.sp1loop0_reg import Sp1Loop0Reg
from hexgonulator.v67.instructions.concrete.sp2loop0_imm import Sp2Loop0Imm
from hexgonulator.v67.instructions.concrete.sp2loop0_reg import Sp2Loop0Reg
from hexgonulator.v67.instructions.concrete.sp3loop0_imm import Sp3Loop0Imm
from hexgonulator.v67.instructions.concrete.sp3loop0_reg import Sp3Loop0Reg
from hexgonulator.v67.instructions.concrete.transfer_from_cr import TransferFromCr
from hexgonulator.v67.instructions.concrete.transfer_pair_from_cr import TransferPairFromCr
from hexgonulator.v67.instructions.concrete.transfer_pair_to_cr import TransferPairToCr
from hexgonulator.v67.instructions.concrete.transfer_to_cr import TransferToCr


def decode_cr_class(instruction):
    bits_27_20 = substring(instruction, 27, 20)
    bits_27_21 = substring(instruction, 27, 21)
    bit_13 = bit_at(instruction, 13)
    bit_7 = bit_at(instruction, 7)
    bit_4 = bit_at(instruction, 4)
    if bits_27_20 == 0b10110000 and bit_13 and bit_7 and bit_4:
        return Q6PFastcorner9Pp
    if bits_27_20 == 0b10110001 and bit_13 and bit_7 and bit_4:
        return Q6PNotFastcorner9Pp
    if bits_27_20 == 0b10111000 and not bit_13:
        return Q6PAny8P
    if bits_27_20 == 0b10111010 and not bit_13:
        return Q6PAll8P
    if bits_27_21 == 0b0000000:
        return Loop0Reg
    if bits_27_21 == 0b0000001:
        return Loop1Reg
    if bits_27_21 == 0b1001000:
        return Loop0Imm
    if bits_27_21 == 0b1001001:
        return Loop1Imm
    if substring(instruction, 27, 16) == 0b101001001001:
        return AddToPc
    if bits_27_21 == 0b0000101:
        return Sp1Loop0Reg
    if bits_27_21 == 0b0000110:
        return Sp2Loop0Reg
    if bits_27_21 == 0b0000111:
        return Sp3Loop0Reg
    if bits_27_21 == 0b1001101:
        return Sp1Loop0Imm
    if bits_27_21 == 0b1001110:
        return Sp2Loop0Imm
    if bits_27_21 == 0b1001111:
        return Sp3Loop0Imm
    if bits_27_20 == 0b10110000 and not bit_13:
        return Q6PAndPp
    if bits_27_20 == 0b10110001 and not bit_13:
        return Q6PAndAndPpp
    if bits_27_20 == 0b10110010 and not bit_13:
        return Q6POrPp
    if bits_27_20 == 0b10110011 and not bit_13:
        return Q6PAndOrPpp
    if bits_27_20 == 0b10110100 and not bit_13:
        return Q6PXorPp
    if bits_27_20 == 0b10110101 and not bit_13:
        return Q6POrAndPpp
    if bits_27_20 == 0b10110110 and not bit_13:
        return Q6PAndPnp
    if bits_27_20 == 0b10110111 and not bit_13:
        return Q6POrOrPpp
    if bits_27_20 == 0b10111001 and not bit_13:
        return Q6PAndAndPpnp
    if bits_27_20 == 0b10111011 and not bit_13:
        return Q6PAndOrPpnp
    if bits_27_20 == 0b10111100 and not bit_13:
        return Q6PNotP
    if bits_27_20 == 0b10111101 and not bit_13:
        return Q6POrAndPpnp
    if bits_27_20 == 0b10111110 and not bit_13:
        return Q6POrPnp
    if bits_27_20 == 0b10111111 and not bit_13:
        return Q6POrOrPpnp
    if bits_27_21 == 0b0010001:
        return TransferToCr
    if bits_27_21 == 0b0011001:
        return TransferPairToCr
    if bits_27_21 == 0b1000000:
        return TransferPairFromCr
    if bits_27_21 == 0b1010000:
        return TransferFromCr
