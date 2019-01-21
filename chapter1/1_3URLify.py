def URLify2(str):
    if not str:return None
    str_list = list(str)
    for i in range(len(str_list)-1,-1,-1):
        if str_list[i] == ' ':
            str_list.pop(i)
            str_list.insert(i,'0')
            str_list.insert(i,'2')
            str_list.insert(i,'%')
    s = "".join(str_list)
    return s



def URLify(str,len):
    num_spaces = 0
    string_list = list(str)

    for char in string_list:
        if char == ' ':
            num_spaces += 1

    if num_spaces == 0:
        return

    string_list.extend(['']*num_spaces*2)
    org_len = len
    len += num_spaces*2
    pos_to_write = len - 1
    for i in range(org_len-1, -1 ,-1):

        if not string_list[i] == ' ':
            string_list[pos_to_write] = string_list[i]
            pos_to_write -= 1
            continue

        if string_list[i] == ' ':
            string_list[pos_to_write] = '0'
            pos_to_write -= 1

            string_list[pos_to_write] = '2'
            pos_to_write -= 1

            string_list[pos_to_write] = '%'
            pos_to_write -= 1

            num_spaces -= 1
            if num_spaces == 0:
                return string_list

    return "".join(string_list)

s = 'mr john smith'
for i in range(1000000):
    URLify2(s)