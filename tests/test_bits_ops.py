import pytest

from hexgonulator.common.bits_ops import substring, to_unsigned, bit_reverse


@pytest.mark.parametrize('bits, msb, lsb, result', [
    (0b10101010101010101010101010101010, 31, 28, 0b1010)
])
def test_substring(bits: int, msb: int, lsb: int, result: int):
    assert substring(bits, msb, lsb) == result


@pytest.mark.parametrize('bits, length, result', [
    (-1, 16, 0xffff),
    (0xffff, 16, 0xffff),
    (-2, 16, 0xfffe),
    (0xfffe, 16, 0xfffe),
    (2, 16, 2),
])
def test_to_unsigned(bits: int, length: int, result: int):
    assert to_unsigned(bits, length) == result


@pytest.mark.parametrize('bits, length, result', [
    (0xff00, 16, 0x00ff),
    (0b1100, 4, 0b0011),
    (0b1010, 4, 0b0101),
    (0b101, 3, 0b101),
    (0b001, 3, 0b100),
])
def test_bit_reverse(bits: int, length: int, result: int):
    assert bit_reverse(bits, length) == result
