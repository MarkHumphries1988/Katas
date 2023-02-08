def vowel_shift(string, number):
    vowel_list = []
    returnString = ""
    count = 0

    for letter in string:
        if letter in ["a", "e", "i", "o", "u"]:
            vowel_list.append(letter)

    for letter in string:
        if letter in ["a", "e", "i", "o", "u"]:
            returnString += vowel_list[(count - number) % (len(vowel_list))]

            count += 1
        else:
            returnString += letter

    return returnString

    pass
