def rec(n,tower_0,tower_1,tower_2):
    """
    The idea here is to use one tower as a buffer while transferring disks from one tower to other.
    If we have to move n elements from tower0 to tower2, we first put n-1 elements in buffer (tower1), then move nth
    element to tower 2 then move all elements from tower1 to tower2 using tower 0 as buffer.

    Time Complexity: T(n) = T(n-1) + O(1) + T(n-1)
    So, if you solve the upper equation the time complexity will come out to O(2^n)
    To understand better the time complexity, draw the recursion tree and see the height of the tree as well as
    how much work we are doing at each level.

    Space complexity:
    Space complexity will be O(n) because of the stack
    :param n:
    :param tower_0: The initial tower from where we have to move n elements
    :param tower_1: The tower used for buffer
    :param tower_2: The destination tower
    :return:
    """
    if n == 1:
        tower_2.append(tower_0.pop())
        return
    rec(n-1,tower_0,tower_2,tower_1)
    rec(1,tower_0,tower_1,tower_2)
    rec(n-1,tower_1,tower_0,tower_2)




a = [9,8,7,6,5,4,3,2,1]
b = []
c = []

rec(5,a,b,c)
print(a,b,c)
