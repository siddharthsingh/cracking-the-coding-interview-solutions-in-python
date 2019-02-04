def binary_to_string(num):
    """
    converts real number between 0 and 1 to binary
    :param num: real number
    :return: 32 bit binary string or error if number cannot be represented in 32 bits
    """
    if not num:return 0.0
    count = 0
    ans = ["0."]
    while num and count<33:
        count += 1
        num *= 2
        digit = int(num//1)
        if digit:
            num %= 1
        ans.append(str(digit))
        if not num:
            return ''.join(ans)

    return "overflow"

print(binary_to_string(0.0))

