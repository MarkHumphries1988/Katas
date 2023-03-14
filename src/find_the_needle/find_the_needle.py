def find_the_needle(haystack, target):
    list = []

    def stringmaker(ministack, tar, string):

        if type(ministack) == dict:
            for key in ministack:
                stringmaker(ministack[key], tar, f'{string}.{key}')
        if type(ministack) == str:
            if tar.lower() in ministack.lower():
                list.append(string)
    for key in haystack:
        stringmaker(haystack[key], target, key)

    return sorted(list)
