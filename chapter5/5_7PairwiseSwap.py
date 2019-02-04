def swap_bits(num):
    odd_mask = 0x5555555555
    even_mask = 0xAAAAAAAAAA
    even_bits = num&even_mask
    odd_bits = num&odd_mask
    num_swapped = (even_bits>>1)|(odd_bits<<1)
    return num_swapped


print(bin(swap_bits(int('1001010011',2))))
print(bin(swap_bits(int('100101',2))))
print(bin(swap_bits(int('1000011',2))))
print(bin(swap_bits(int('01010011',2))))