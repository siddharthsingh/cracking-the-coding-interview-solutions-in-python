def checkPerm(str1,str2):
    if not len(str1) == len(str2):
        return False
    chars1 = {}
    chars2 = {}
    for char in str1:
        if char not in chars1:
            chars1[char] = 1
        else:
            chars1[char] += 1

    for char in str2:
        if char not in chars2:
            if char not in chars1:
                return False
            chars2[char] = 1
        else:
            chars2[char] += 1
            if chars2[char] > chars1[char]:
                return False
    #
    # for key,value in chars1.items():
    #     if not value == chars2[key]:
    #         return False

    return True


print(checkPerm('a','A'))