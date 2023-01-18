
def caesar(string, number):
    returnstring=""

    for letter in string:
        upper=0
        if 61<=ord(letter.lower())<=122:
            if letter.isupper()==True:
                upper=1
            newletter=(ord(letter.lower())+number)

            if newletter>122:
                newletter=newletter%122+96

            if newletter<97:
                newletter=122-(96-newletter%97)
            
            if upper==1:
                returnstring+=chr(newletter).upper()
            else:
                returnstring+=chr(newletter)
        else:
            returnstring+=letter
    return returnstring
    pass


