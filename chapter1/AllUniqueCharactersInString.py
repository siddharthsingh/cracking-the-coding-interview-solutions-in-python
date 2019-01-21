


def TestUniqueCharacters(characters):
    chars = set()
    charsadd = chars.add
    for character in characters:
        if character not in chars:
            charsadd(character)
        else:
            return False
    return True

def TestUniqueCharacters3WithoutAnyDS(characters):
    characters.sort()
    for i in range(len(characters)-1):
        if characters[i] == characters[i+1]:
            return False
    return True

def TestUniqueCharacters3WithoutAnyDS(characters):
    ans = 0
    for char in characters:
        ans

def TestUniqueCharacters2(characters):
    chars = {}
    for character in characters:
        if character not in chars:
            chars[character] = 1
        else:
            return False
    return True

# for i in range(30000000):
#     TestUniqueCharacters3WithoutAnyDS("qwertyuiopasdfghjklzxcvbnm1234567890-=[];',.!@#$%^&*()")

print(TestUniqueCharacters3WithoutAnyDS("qwertyuiopasdfghjklzxcvbnm1234567890-=[];',.!@#$%^&*()"))