def lower_chunk(bits: int, chunk_length: int) -> int:
    return bits & ((2 ** chunk_length) - 1)


def substring(bits: int, msb: int, lsb: int) -> int:
    return lower_chunk(bits, msb + 1) >> lsb


def chain(higher: int, lower: int, lower_length: int) -> int:
    return (higher << lower_length) + lower


def to_signed(bits: int, length: int) -> int:
    real_num_length = (length - 1)
    negative_bit = bits >> real_num_length
    if negative_bit:
        # Negative
        return (bits - (negative_bit << real_num_length)) - (2 ** real_num_length)
    else:
        return bits


def to_unsigned(bits: int, length: int) -> int:
    return bits % (2 ** length)


def bit_not(bits: int, length: int) -> int:
    return bits ^ ((1 << length) - 1)


def set_substring(bits: int, msb: int, lsb: int, value: int) -> int:
    mask_length = msb + 1 - lsb
    mask = ((2 ** mask_length) - 1) << lsb
    return (bits & bit_not(mask, 256)) | value << lsb


def bit_at(bits: int, index: int) -> int:
    return substring(bits, index, index)


def set_bit_at(bits: int, index: int, value: int) -> int:
    return set_substring(bits, index, index, value)


def signed_sat_q(i: int, n: int):
    if i > (2 ** (n - 1) - 1):
        result = 2 ** (n - 1) - 1
        saturated = True
    elif i < -1 * (2 ** (n - 1)):
        result = -1 * (2 ** (n - 1))
        saturated = True
    else:
        result = i
        saturated = False
    return to_unsigned(result, n), saturated


def unsigned_sat_q(i: int, n: int):
    if i > (2 ** n - 1):
        result = 2 ** n - 1
        saturated = True
    elif i < 0:
        result = 0
        saturated = True
    else:
        result = i
        saturated = False
    return result, saturated


def sign_extend(x: int, src_length: int, dst_length: int) -> int:
    return to_unsigned(to_signed(x, src_length), dst_length)
