def find_partner(list, directions):
    directionDict = {'up': [-1, 0], 'down': [1, 0],
                     'left': [0, -1], 'right': [0, 1]}
    names = []
    if len(directions) == 0:
        return []
    currentPosition = [0, 0]
    for direction in directions:
        currentPosition[1] = (currentPosition[1] +
                              directionDict[direction][1]) % len(list[0])

        if 0 <= (currentPosition[0] + directionDict[direction][0]) < len(list):
            currentPosition[0] += directionDict[direction][0]
            names.append(list[currentPosition[0]][currentPosition[1]])

    return names
    pass
