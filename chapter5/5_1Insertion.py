def insertion(num1,num2,i,j):
    for ii in range(j,i+1):
        print(bin((num2&(1<<(ii-j)))>>(ii-j)))
        num1 = set_bit(num1,(num2&(1<<(ii-j)))>>(ii-j),ii)
    return num1

def clear_bit(num, bit_index):
    return (num&~(1<<bit_index))

def set_bit(num, bit, index):
    return (num&~(1<<index))|(bit<<index)


print(bin(insertion(64,19,5,1)))