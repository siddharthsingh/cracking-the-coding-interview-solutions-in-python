def multiply(num1,num2):
    if num1==0 or num2 == 0:
        return 0
    n = num2
    num = num1
    count = 0
    while n>>1:
        num1 <<= 1
        n >>= 1
        count+=1
    # print(num1,count)
    global store
    store[1] = num
    store[0] = 0

    if count:
        remaining = num2 - 2**count
        return num1 + rec(num, remaining)
    else:
        remaining = num2


    return rec(num,remaining)
store = {}

def rec(num1,num2):
    global store
    # print(num1,num2)
    if num2 in store:
        return store[num2]
    mid = num2//2
    a = rec(num1,mid)
    b = rec(num1,num2-mid)
    store[num2] = a+b
    return a+b

# print(multiply(50,110))
# assert multiply(5,10)==5*10, "Not equal"
# assert multiply(50,110)==50*110, "Not equal"
# assert multiply(5,1)==5*1, "Not equal"
assert multiply(15,2)==15*2, "Not equal"