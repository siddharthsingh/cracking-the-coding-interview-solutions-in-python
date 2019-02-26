def create_perms(self, string, pos):
    if pos == len(string) - 1:
        return [[string[pos]]]
    a = self.create_perms(string, pos + 1)
    ans = []
    for aa in a:
        i = len(aa)
        while i >= 0:
            caa = aa[:]
            caa.insert(i, string[pos])
            if caa not in ans:
                ans.append(caa)
            i = i - 1
    return ans

# not the best solution