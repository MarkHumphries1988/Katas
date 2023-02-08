import math


def encrypt(str, n):
    if n == 0:
        return str
    else:
        startStr = ""
        endStr = ""
        for index, letter in enumerate(str):
            if index % 2 == 0:
                endStr += letter
            else:
                startStr += letter
        return encrypt(startStr + endStr, n - 1)
    pass


# EXTENSION


def decrypt(str, n):
    if n == 0:
        return str
    else:
        returnStr = ""
        half = math.floor(len(str)/2)
        for i in range(half):
            returnStr += str[half + i] + str[i]
        if len(str) % 2 != 0:
            returnStr += str[-1]
    return decrypt(returnStr, n-1)

    pass
