def StringCompression(str1):
    if len(str1)<3:return str1
    prev_char = str1[0]
    prev_char_count = 1
    res = []
    for char in str1[1:]:
        if char == prev_char:
            prev_char_count+=1
        else:
            res.append(prev_char + str(prev_char_count))
            prev_char_count = 1
            prev_char = char

    res.append(prev_char + str(prev_char_count))
    res = "".join(res)
    return  res if len(res)<len(str1) else str1

print(StringCompression('aabbbbcdd'))
print(StringCompression('abcdefgh'))
print(StringCompression('ab'))
print(StringCompression('aaaaaaa'))
print(StringCompression(''))
print(StringCompression('aabbcc'))
