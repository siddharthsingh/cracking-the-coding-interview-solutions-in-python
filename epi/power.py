def power(x,y):
    if y == 0:
        return 1
    if y<0:
        x = 1/x
        y = -y
    cur_power = 2
    ans = x
    while cur_power<y:
        ans *= ans
        cur_power *= 2

    return ans*power(x,y-cur_power/2)



print(power(2.1,-5),2.1**-5)
