def stringRotation(str1,str2):
    if not str1 or len(str1)!= len(str2):return False

    for i,char in enumerate(str1):
        wrong = False
        for j in range(len(str1)):
            if str1[(j+i)%len(str1)] != str2[j]:
                wrong = True

        if not wrong:
            return True

    return False

def stringRotation2(str1,str2):
    a = list(str1).sort()
    b = list(str2).sort()
    return sorted(list(str1))== sorted(list(str2))
def stringRotation3(str1,str2):
    return str1 in str2+str2
print(stringRotation3('waterbottle','lxwaterbott'))


