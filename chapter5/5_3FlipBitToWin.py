def max_ones_on_one_flip(number,size):
    max_count = float('-inf')
    zero_fount_at = -1
    zero_found = False
    count = 0
    i=0
    while i < size:
        bit = get_bit(number,i)
        # print(i,bit,zero_fount_at,count)

        if zero_found and bit == 0:
            if count > max_count:
                max_count = count
            count = 0
            zero_found = False
            i = zero_fount_at
        elif bit == 0:
            zero_found = True
            zero_fount_at = i
            count += 1
        else:
            count += 1
        i += 1
    return max_count if max_count>count else count

def get_bit(number,index):
    return (number&(1<<index))>>index


print(max_ones_on_one_flip(int('11111101001111',2),14))