
def herd_the_babies(string):
    herddict={}
    herded=""
    for character in string:
        if character.upper() in herddict:
            if character.islower():
                herddict[character.upper()][1]+=1
            else:
                herddict[character.upper()][0]+=1
        else:
            if character.islower():
                herddict[character.upper()]=[0,1]
            else:
                herddict[character.upper()]=[1,0]

    dictkeys=list(herddict.keys())
    dictkeys.sort()
    sorted_herddict={letter:herddict[letter] for letter in dictkeys}

    for key in sorted_herddict:
        herded+=key.upper()*sorted_herddict[key][0]+key.lower()*sorted_herddict[key][1]

    return herded



    
    

    pass
