def sentence_to_camel_case(arg1, *arg2,reverse=False):
    finalStr=""
    if len(arg2)>0:
        list=arg1.split(" ")
        if arg2[0]==True:
            for word in list:
                finalStr+=word[0].upper()+word[1:]
        elif arg2[0]==False:
            finalStr+=list[0][0].lower()+list[0][1:]

            for word in list[1:]:
                finalStr+=word[0].upper()+word[1:]
    if reverse != False:
       
        finalStr+=arg1[0][0].upper()
        
        for letter in arg1[1:]:
            if letter.isupper()==True:
                finalStr+=" "+letter.lower()
            else:
                finalStr+=letter
        finalStr+="."
    
            



    return finalStr


    pass
