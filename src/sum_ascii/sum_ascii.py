
def sum_ascii(array):
    currentwinner=""
    highscore=0

    for name in array:
        namescore=0
        for letter in name:
            namescore+=ord(letter.lower())
        if(namescore>highscore):
            currentwinner=name
            highscore=namescore
    return currentwinner
    pass
