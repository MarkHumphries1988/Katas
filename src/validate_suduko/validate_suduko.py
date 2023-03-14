
def validate_suduko(suduko):
    if len(suduko) < 9:
        return False
    for i in range(9):
        if len(suduko[i]) < 9:
            return False

    squares = [[] for _ in range(9)]
    squarecount = 0
    for i in [1, 4, 7]:
        for j in [1, 4, 7]:
            for k in range(3):
                for m in range(3):
                    squares[squarecount].append(suduko[i - 1 + k][j - 1 + m])

            squarecount += 1

    print(squares)

    for i in range(9):
        column = [suduko[i][j] for j in range(9)]

        for j in range(1, 10):
            if (j) not in suduko[i] or (
                    j) not in column or (j) not in squares[i]:
                return False
    return True

    pass
