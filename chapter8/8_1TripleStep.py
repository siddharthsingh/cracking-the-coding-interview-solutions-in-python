def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0 or n == 1:
        return 1
    a = 1
    b = 1
    c = 2
    for i in range(3, n + 1):
        d = a + b + c
        a,b,c = b,c,d
    return d