"""Functions to implement VLQ coding/decoding.
   Note: This was made with AI help.
"""

def encode(numbers):
    """
    Encode a list of unsigned 32-bit integers using Variable Length Quantity (VLQ).

    Each integer is converted into one or more bytes. Only the lower 7 bits
    of each byte store data. The most significant bit (MSB) is used as a
    continuation flag:
        - MSB = 1 → more bytes follow for this number
        - MSB = 0 → this is the last byte of the number

    Numbers between 0 and 127 are encoded as a single byte.
    Larger numbers are split into 7-bit groups and encoded in big-endian order.

    :param numbers: list[int]
        A list of unsigned integers (0 ≤ n ≤ 0xFFFFFFFF).

    :return: list[int]
        A list of bytes (integers between 0 and 255) representing
        the VLQ-encoded values.
    """
    result = []
    for number in numbers:
        if number == 0:
            result.append(0)
            continue
        chunks = []
        # Break number into 7-bit groups (least significant first)
        count = number
        while count > 0:
            chunks.append(count & 0x7F) #0x7F = 01111111
            count >>= 7
        # Reverse to make most significant group first
        chunks.reverse()
        # Set continuation bit (MSB) on all but last byte
        for index in range(len(chunks) - 1):
            result.append(chunks[index] | 0x80) #0x80 = 10000000
        # Last byte (MSB = 0)
        result.append(chunks[-1])
    return result


def decode(bytes_):
    """
    Decode a list of bytes encoded using Variable Length Quantity (VLQ).

    The function reconstructs integers by reading 7-bit groups from
    each byte. The most significant bit (MSB) indicates whether the
    current number continues:
        - MSB = 1 → continue reading bytes
        - MSB = 0 → this is the final byte of the current number

    When a byte with MSB = 0 is encountered, the accumulated value
    is appended to the result list.

    :param bytes_: list[int]
        A list of bytes (integers between 0 and 255) representing
        VLQ-encoded numbers.

    :return: list[int]
        The decoded list of unsigned integers.

    :raises ValueError:
        If the byte sequence ends before a number is fully decoded
        (i.e., an incomplete sequence is detected).
    """
    result = []
    current = 0
    has_started = False
    for byte in bytes_:
        has_started = True
        # Add 7 bits to current number
        current = (current << 7) | (byte & 0x7F) # & deletes MSB. | rebuild the number.
        # If MSB is 0 → this is the last byte of the number
        if (byte & 0x80) == 0:
            result.append(current)
            current = 0
            has_started = False
    # If we finished but last number never ended → error
    if has_started:
        raise ValueError("incomplete sequence")
    return result