def mask(*args):

    def inner(*funargs):

        def fake_func(*whoknows):
            if len(whoknows) > 0:
                unmasked = funargs[0](whoknows[0])
            else:
                unmasked = funargs[0]()
            masker(unmasked, args)

            return unmasked
        return fake_func

    return inner


def masker(mini, tomask):
    for key in mini:
        # mini[key] = "".join(["*" if c != " "
        #                     else " " for c in mini[key]])
        for mask in tomask:
            if key == mask:
                mini[key] = "".join(["*" if c != " "
                                    else " " for c in mini[key]])
        if type(mini[key]) == dict:
            masker(mini[key], tomask)
