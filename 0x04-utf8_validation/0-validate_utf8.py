#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    number_bytes = 0

    # Define masks for UTF-8 encoding
    start_byte_mask = 1 << 7
    continuation_byte_mask = 1 << 6

    for byte in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            # Count number of bytes in the sequence
            while mask_byte & byte:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            # Check for invalid number of bytes
            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            # Check if byte is a continuation byte
            if not (byte & start_byte_mask and not (byte & continuation_byte_mask)):
                return False

        number_bytes -= 1

    # Check if all bytes have been processed
    if number_bytes == 0:
        return True

    return False
