#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    It determines whether given data set represents valid UTF-8 encoding
    """
    num_bytes = 0

    first_mask = 1 << 7
    second_mask = 1 << 6

    for byte in data:

        mask_byte = 1 << 7

        if num_bytes == 0:

            while mask_byte & byte:
                num_bytes += 1
                mask_byte >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (byte & first_mask and not (byte & second_mask)):
                    return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
