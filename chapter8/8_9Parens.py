def faster_sol(self, to_open, to_close):
    if not to_open and not to_close:
        return ['']
    if not to_open and to_close:
        return [')' * to_close]
    res = []
    if to_close - to_open:
        a = self.faster_sol(to_open - 1, to_close)
        if a:
            res.extend(['(' + s for s in a])
        b = self.faster_sol(to_open, to_close - 1)
        if b:
            res.extend([')' + s for s in b])
    else:
        a = self.faster_sol(to_open - 1, to_close)
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