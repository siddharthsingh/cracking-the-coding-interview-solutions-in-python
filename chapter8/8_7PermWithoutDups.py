def create_perms(string,pos):
    if pos == len(string)-1:
        return [[string[pos]]]
    a = create_perms(string,pos+1)
    ans = []
    for aa in a:
        i = len(aa)
        while i>=0:
            caa = aa[:]
            caa.insert(i,string[pos])
            ans.append(caa)
            i = i-1
    return ans

print(create_perms(list("abc"),0))
