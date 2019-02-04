def next_largest(number,size):
    first_one_found = False
    for i in range(size):
        bit = get_bit(number,i)
        if bit == 0 and first_one_found:
            number = clear_bit(number,i-1)
            number = set_bit_one(number,i)
            return number
        elif bit:
            first_one_found = True
    return number


def next_smallest(number,size):
    first_zero_fount = False
    for i in range(size):
        bit = get_bit(number,i)
        if bit and first_zero_fount:
            number = clear_bit(number,i)
            number = set_bit_one(number,i-1)
            return number
        elif not bit:
            first_zero_fount = True
    return number


def get_bit(number, index):
    return (number & (1 << index)) >> index

def clear_bit(number,index):
    return number&~(1<<index)
def set_bit_one(number, index):
    return number|(1<<index)

print(bin(next_smallest(int('10001',2),5)))