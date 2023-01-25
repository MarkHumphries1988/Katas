def reduce_by_steps(binfunc, list, initial):
    if len(list) < 2:
        return initial
    first = initial+binfunc(list[0], list[1])
    for element in list[2:]:
        first = binfunc(first, element)

    return first
    pass
