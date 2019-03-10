def faster_sol(to_open, to_close):
    """
    This algorithm we keep track of open parenthesis(left '(' ) and close parenthesis
    At each step we have two options to add '(' to the result or ')'.
    We only add ')' if the number of to open is less, that means we have used more '(' than ')'

    The time complexity of this algorithm should be O(2^n)
    T(n) = 2T(n-1)
    Space complexity would be O(n) for stack, if we ignore the space required for output.
    :param to_open:
    :param to_close:
    :return:
    """
    if not to_open and not to_close:
        return ['']
    if not to_open and to_close:
        return [')' * to_close]
    res = []
    if to_close - to_open:
        a = faster_sol(to_open - 1, to_close)
        if a:
            res.extend(['(' + s for s in a])
        b = faster_sol(to_open, to_close - 1)
        if b:
            res.extend([')' + s for s in b])
    else:
        a = faster_sol(to_open - 1, to_close)
        if a:
            res.extend(['(' + s for s in a])
    return res


def rec(self, n):
    if n == 1:
        return [['(', ')']]
    a = self.rec(n - 1)
    ans = []
    for aa in a:
        i = len(aa)
        while i >= 0:
            caa = aa[:]
            caa.insert(i, ')')
            caa.insert(i, '(')
            if caa not in ans:
                ans.append(caa)
            i -= 1
    return sorted(ans)
n = 5
print(len(faster_sol(n,n)))