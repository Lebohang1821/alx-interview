#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    num_bytes = 0
    max_bytes = 4

    start_byte_mask = 1 << 7
    continuation_byte_mask = (1 << 7) | (1 << 6)

    for byte in data:

        mask_byte = 1 << 7

        if num_bytes == 0:

            while mask_byte & byte:
                num_bytes += 1
                mask_byte = mask_byte >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > max_bytes:
                return False

        else:
            if not (byte & start_byte_mask and not (byte & continuation_byte_mask)):
                return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
