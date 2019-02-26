def rec(n,s0,s1,s2):
    if n == 1:
        s2.append(s0.pop())
        return
    rec(n-1,s0,s2,s1)
    rec(1,s0,s1,s2)
    rec(n-1,s1,s0,s2)




a = [9,8,7,6,5,4,3,2,1]
b = []
c = []

rec(5,a,b,c)
print(a,b,c)
