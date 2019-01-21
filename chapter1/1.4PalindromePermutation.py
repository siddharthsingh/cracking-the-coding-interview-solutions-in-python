def PalindromePermutation(str):

    char_freq = {}
    for char in str:
        if char == " ":
            continue
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1

    one_odd_allowed_found = False
    for key,value in char_freq.items():
        if value%2:
            if one_odd_allowed_found:
                return False
            else:
                one_odd_allowed_found = True



    return True



print(PalindromePermutation("taaatt"))