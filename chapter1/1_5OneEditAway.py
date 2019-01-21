def OneEditAway(str1,str2):
    if not str1 and not str2:return False
    if abs(len(str1) - len(str2)) > 1:return False
    pointer_1 = 0
    pointer_2 = 0
    min_len = min(len(str1),len(str2))
    one_diff_found = False
    while pointer_1<min_len or pointer_2<min_len:
        if str1[pointer_1] == str2[pointer_2]:
            pointer_1+=1
            pointer_2 += 1
        elif not one_diff_found:

            one_diff_found = True
            if pointer_1+1<len(str1)-1:
                if str1[pointer_1+1] == str2[pointer_2]:
                    pointer_1+=1
                    continue
            if pointer_2+1<len(str2)-1:
                if str2[pointer_2+1] == str1[pointer_1]:
                    pointer_2+=1
                    continue

            if pointer_2+1<len(str2)-1 and pointer_1+1<len(str1)-1 and str1[pointer_1+1]==str2[pointer_2+1]:
                pointer_2+=2
                pointer_1+=2
                continue
            else:
                if pointer_1==len(str1)-1 or pointer_2==len(str2)-1 :
                    return True
                return False
        else:
            return False
    return True

print(OneEditAway('plex','plex'))
print(OneEditAway('ple','plex'))
print(OneEditAway('plex','ple'))
print(OneEditAway('plef','plex'))
print(OneEditAway('abcd','afgd'))
print(OneEditAway('pale','bale'))
print(OneEditAway('apple','aple'))
