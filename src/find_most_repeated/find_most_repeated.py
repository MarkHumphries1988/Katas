def find_most_repeated(list):
    dict = {'elements': [], 'repeats': 2}

    for word in list:
        if list.count(word) == dict['repeats']:
            dict['elements'].append(word)
            dict['repeats'] = list.count(word)
            list = [newword for newword in list if newword != word]
        if list.count(word) > dict['repeats']:
            dict['elements'] = [word]
            dict['repeats'] = list.count(word)
            list = [newword for newword in list if newword != word]

    if len(dict['elements']) == 0:
        dict['repeats'] = 'null'
    print(dict)
    return dict
    pass
