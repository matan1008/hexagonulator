import pytest

from hexgonulator.common.bits_ops import substring


@pytest.mark.parametrize('bits, msb, lsb, result', [
    (0b10101010101010101010101010101010, 31, 28, 0b1010)
])
def test_substring(bits: int, msb: int, lsb: int, result: int):
    assert substring(bits, msb, lsb) == result
