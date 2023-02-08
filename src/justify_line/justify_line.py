import re


def justify_line(str, length):
    if len(str) > length:
        return "String exceeds maximum line length"
    returnstr = ""
    list = re.findall(r'\S+', str)
    list2 = re.findall(r'\s+', str)
    spaces = length - len(str)
    for i in range(spaces):
        list2[i % len(list2)] += " "
    for i in range(len(list2)):
        returnstr += list[i] + list2[i]

    return returnstr + list[-1]

    pass
