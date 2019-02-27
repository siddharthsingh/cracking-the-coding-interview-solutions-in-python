def rec_mul(num1,num2):
    """
    The idea behind this recursive multiply is simple. If num2 is divisible by 2 we calculate the multiplication result
    of num1 and num2/2 and then double the result.
    If num2 is odd we do the same as even and then add num1 in the end
    """
    if num2 == 1:
        return num1
    if num2%2:
        num2 = num2>>1
        return (rec_mul(num1,num2)<<1)+num1
    else:
        num2 = num2>>1
        return rec_mul(num1,num2)<<1

def mul(num1,num2):
    """
    The time complexity of this algorithm is O(log s) where s i s smaller number.
    That is why we check which number is smaller initaially before calling rec_mul
    :param num1:
    :param num2:
    :return:
    """
    return rec_mul(num1,num2) if num1>num2 else rec_mul(num2,num1)
print(rec_mul(5,10),5*10)
assert rec_mul(5,10)==5*10, "Not equal"
assert rec_mul(50,110)==50*110, "Not equal"
assert rec_mul(5,1)==5*1, "Not equal"
assert rec_mul(15,2)==15*2, "Not equal"