def diff_bits(num1,num2,size):
    count = 0
    for i in range(size):
        if get_bit(num1,i) != get_bit(num2,i):
            count += 1
    return count

def get_bit(num,index):
    return (num&(1<<index))>>index

print(diff_bits(int('11101',2),int('01111',2),5))