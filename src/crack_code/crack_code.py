import re


def crack_code(encrypt):
    endingKey = encrypt[-5:-1]
    chain = encrypt[:-6]

    if endingKey != ''.join(sorted(endingKey)):
        return False
    chain = re.sub("[^a-z]", "-", chain)
    chain = sorted(chain.split("-"), key=lambda e: (-len(e), e))

    filterChain = [letter for letter in chain if len(letter) >= len(chain[3])]
    for index, letter in enumerate(endingKey):
        if letter != filterChain[index][0]:
            return False

    return True
