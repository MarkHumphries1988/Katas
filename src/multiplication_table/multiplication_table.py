def multiplication_table(number):
    returnList = []
    if number == 0:
        return returnList
    number = number+1
    for i in range(number):
        returnList.append([i if j == 0 else j if i == 0 else i*j
                           for j in range(number)])
    print(returnList)
    return returnList
    pass
