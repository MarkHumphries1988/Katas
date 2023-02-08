import math


def binary_search(list, target, position=0):
    if len(list) == 0:
        return -1
    print(position)

    mid = math.floor(len(list)/2)

    if list[mid] == target:
        return mid+position

    if list[mid] >= target:
        return binary_search(list[0:mid], target, position)

    else:
        return binary_search(list[mid+1:], target, position+mid+1)
    pass
