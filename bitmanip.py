
all_ones = 0b11111111
all_zeros = 0b00000000

def set_bit(bitfield, pos):
    mask = all_zeros | 1 << pos
    bitfield |= mask
    return bitfield

def clear_bit(bitfield, pos):
    mask = !(all_zeros | 1 << pos)
    bitfield &= mask
    return bitfield

def is_set(bitfield, pos):
    mask = all_zeros | 1 << pos
    return ((bitfield | mask) is not False)

