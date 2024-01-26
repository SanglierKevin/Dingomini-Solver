def rotate(matrix):
    try:
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                matrix[x][y] = rotate(matrix[x][y])
    finally:
        return [list(row) for row in zip(*matrix[::-1])]


def printM(matrix):
    for a in range(len(matrix)):
        if (matrix[a][0] == tile0):
            break
        for b in range(2):
            for c in range(len(matrix[0])):
                for d in range(2):
                    print(color(matrix[a][c][b][d]), end="")
            print("")
    print("")


def color(code):
    match code:
        case 1:
            return "\x1b[1;34m" + u"\u2588" + "\x1b[0m"
        case 2:
            return "\x1b[1;30m" + u"\u2588" + "\x1b[0m"
        case 3:
            return "\x1b[1;35m" + u"\u2588" + "\x1b[0m"
        case 4:
            return "\x1b[1;32m" + u"\u2588" + "\x1b[0m"
        case 5:
            return "\x1b[1;31m" + u"\u2588" + "\x1b[0m"
        case 6:
            return "\x1b[1;33m" + u"\u2588" + "\x1b[0m"
        case 0:
            return ""


def checkHorizontal(line):
    line1 = [game[line][0][0][0], game[line][0][0][1], game[line][1][0][0], game[line][1][0][1], game[line][2][0][0], game[line][2][0][1]]
    line1 = list(filter((0).__ne__, line1))
    line2 = [game[line][0][1][0], game[line][0][1][1], game[line][1][1][0], game[line][1][1][1], game[line][2][1][0], game[line][2][1][1]]
    line2 = list(filter((0).__ne__, line2))
    if len(line1) != len(set(line1)) or len(line2) != len(set(line2)):
        return False
    return True


def checkVertical(column):
    col1 = [game[0][column][0][0], game[0][column][1][0], game[1][column][0][0], game[1][column][1][0], game[2][column][0][0], game[2][column][1][0]]
    col1 = list(filter((0).__ne__, col1))
    col2 = [game[0][column][0][1], game[0][column][1][1], game[1][column][0][1], game[1][column][1][1], game[2][column][0][1], game[2][column][1][1]]
    col2 = list(filter((0).__ne__, col2))
    if len(col1) != len(set(col1)) or len(col2) != len(set(col2)):
        return False
    return True


def checkOblique(cards):
    if cards == 4:
        obl1 = [game[0][0][0][0], game[0][0][1][1], game[1][1][0][0], game[1][1][1][1]]
        obl1 = list(filter((0).__ne__, obl1))
        obl2 = [game[1][0][1][0], game[1][0][0][1], game[0][1][1][0], game[0][1][0][1]]
        obl2 = list(filter((0).__ne__, obl2))

        if len(obl1) != len(set(obl1)) or len(obl2) != len(set(obl2)):
            return False
        return True

    elif cards == 6:
        obl3 = [game[0][0][0][0], game[0][0][1][1], game[1][1][0][0], game[1][1][1][1]]
        obl3 = list(filter((0).__ne__, obl3))
        obl4 = [game[0][1][0][0], game[0][1][1][1], game[1][2][0][0], game[1][2][1][1]]
        obl4 = list(filter((0).__ne__, obl4))
        obl5 = [game[1][0][1][0], game[1][0][0][1], game[0][1][1][0], game[0][1][0][1]]
        obl5 = list(filter((0).__ne__, obl5))
        obl6 = [game[1][1][1][0], game[1][1][0][1], game[0][2][1][0], game[0][2][0][1]]
        obl6 = list(filter((0).__ne__, obl6))

        if len(obl3) != len(set(obl3)) or len(obl4) != len(set(obl4)) or len(obl5) != len(set(obl5)) or len(obl6) != len(set(obl6)):
            return False
        return True

    elif cards == 9:
        obl7 = [game[0][0][0][0], game[0][0][1][1], game[1][1][0][0], game[1][1][1][1], game[2][2][0][0], game[2][2][1][1]]
        obl7 = list(filter((0).__ne__, obl7))
        obl8 = [game[2][0][1][0], game[2][0][0][1], game[1][1][1][0], game[1][1][0][1], game[0][2][1][0], game[0][2][0][1]]
        obl8 = list(filter((0).__ne__, obl8))

        if len(obl7) != len(set(obl7)) or len(obl8) != len(set(obl8)):
            return False
        return True


def checkRotate(list):
    test = game.copy()
    for x in range(4):
        if rotate(test) in list:
            return False
    return True


# Vide = 0
# Bleu = 1
# Gris = 2
# Rose = 3
# Vert = 4
# Rouge = 5
# Jaune = 6
tile1 = [[5, 6],
         [3, 5]]

tile2 = [[2, 4],
         [1, 2]]

tile3 = [[2, 6],
         [1, 4]]

tile4 = [[1, 4],
         [6, 3]]

tile5 = [[4, 6],
         [5, 3]]

tile6 = [[3, 1],
         [6, 5]]

tile7 = [[2, 4],
         [5, 3]]

tile8 = [[3, 2],
         [1, 4]]

tile9 = [[5, 1],
         [2, 6]]

tile0 = [[0, 0],
         [0, 0]]

tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9]

sol4List = []
sol4Found = 0
sol6List = []
sol6Found = 0
sol9List = []
sol9Found = 0

print("\nTiles :")

for x in tiles:
    printM([[x]])

posUpLeft = tile0
posUpCenter = tile0
posUpRight = tile0
posMiddleLeft = tile0
posMiddleCenter = tile0
posMiddleRight = tile0
posBottomLeft = tile0
posBottomCenter = tile0
posBottomRight = tile0
game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]

for a in tiles:
    cleanTiles1 = tiles.copy()
    posUpLeft = a
    cleanTiles1.remove(a)
    for xa in range(4):
        posUpLeft = rotate(posUpLeft)

        for b in cleanTiles1:
            cleanTiles2 = cleanTiles1.copy()
            posUpCenter = b
            cleanTiles2.remove(b)
            for xb in range(4):
                posUpCenter = rotate(posUpCenter)

                for c in cleanTiles2:
                    game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                    if checkHorizontal(0) == False:
                        break
                    cleanTiles3 = cleanTiles2.copy()
                    posMiddleLeft = c
                    cleanTiles3.remove(c)
                    for xc in range(4):
                        posMiddleLeft = rotate(posMiddleLeft)

                        for d in cleanTiles3:
                            game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                            if checkVertical(0) == False:
                                break
                            posMiddleCenter = d
                            for xd in range(4):
                                posMiddleCenter = rotate(posMiddleCenter)

                                game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                                if checkHorizontal(1) == False:
                                    break
                                if checkVertical(1) == False:
                                    break
                                if checkOblique(4) == False:
                                    break
                                if checkRotate(sol4List) == False:
                                    break
                                sol4Found += 1
                                sol4List.append(game)

posUpLeft = tile0
posUpCenter = tile0
posUpRight = tile0
posMiddleLeft = tile0
posMiddleCenter = tile0
posMiddleRight = tile0
posBottomLeft = tile0
posBottomCenter = tile0
posBottomRight = tile0
game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]

for a in tiles:
    cleanTiles1 = tiles.copy()
    posUpLeft = a
    cleanTiles1.remove(a)
    for xa in range(4):
        posUpLeft = rotate(posUpLeft)

        for b in cleanTiles1:
            cleanTiles2 = cleanTiles1.copy()
            posUpCenter = b
            cleanTiles2.remove(b)
            for xb in range(4):
                posUpCenter = rotate(posUpCenter)

                for c in cleanTiles2:
                    cleanTiles3 = cleanTiles2.copy()
                    posUpRight = c
                    cleanTiles3.remove(c)
                    for xc in range(4):
                        posUpRight = rotate(posUpRight)

                        for d in cleanTiles3:
                            game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                            if checkHorizontal(0) == False:
                                break
                            cleanTiles4 = cleanTiles3.copy()
                            posMiddleLeft = d
                            cleanTiles4.remove(d)
                            for xd in range(4):
                                posMiddleLeft = rotate(posMiddleLeft)

                                for e in cleanTiles4:
                                    game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                                    if checkVertical(0) == False:
                                        break
                                    cleanTiles5 = cleanTiles4.copy()
                                    posMiddleCenter = e
                                    cleanTiles5.remove(e)
                                    for xe in range(4):
                                        posMiddleCenter = rotate(posMiddleCenter)

                                        for f in cleanTiles5:
                                            game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                                            if checkVertical(1) == False:
                                                break
                                            posMiddleRight = f
                                            for xf in range(4):
                                                posMiddleRight = rotate(posMiddleRight)

                                                game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                                                if checkHorizontal(1) == False:
                                                    break
                                                if checkVertical(2) == False:
                                                    break
                                                if checkOblique(6) == False:
                                                    break
                                                if checkRotate(sol6List) == False:
                                                    break
                                                sol6Found += 1
                                                sol6List.append(game)

posUpLeft = tile0
posUpCenter = tile0
posUpRight = tile0
posMiddleLeft = tile0
posMiddleCenter = tile0
posMiddleRight = tile0
posBottomLeft = tile0
posBottomCenter = tile0
posBottomRight = tile0
game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]

for a in tiles:
    cleanTiles1 = tiles.copy()
    posUpLeft = a
    cleanTiles1.remove(a)
    for xa in range(4):
        posUpLeft = rotate(posUpLeft)

        for b in cleanTiles1:
            cleanTiles2 = cleanTiles1.copy()
            posUpCenter = b
            cleanTiles2.remove(b)
            for xb in range(4):
                posUpCenter = rotate(posUpCenter)

                for c in cleanTiles2:
                    cleanTiles3 = cleanTiles2.copy()
                    posUpRight = c
                    cleanTiles3.remove(c)
                    for xc in range(4):
                        posUpRight = rotate(posUpRight)

                        for d in cleanTiles3:
                            game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                            if checkHorizontal(0) == False:
                                break
                            cleanTiles4 = cleanTiles3.copy()
                            posMiddleLeft = d
                            cleanTiles4.remove(d)
                            for xd in range(4):
                                posMiddleLeft = rotate(posMiddleLeft)

                                for e in cleanTiles4:
                                    cleanTiles5 = cleanTiles4.copy()
                                    posMiddleCenter = e
                                    cleanTiles5.remove(e)
                                    for xe in range(4):
                                        posMiddleCenter = rotate(posMiddleCenter)

                                        for f in cleanTiles5:
                                            cleanTiles6 = cleanTiles5.copy()
                                            posMiddleRight = f
                                            cleanTiles6.remove(f)
                                            for xf in range(4):
                                                posMiddleRight = rotate(posMiddleRight)

                                                for g in cleanTiles6:
                                                    game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                                                    if checkHorizontal(1) == False:
                                                        break
                                                    cleanTiles7 = cleanTiles6.copy()
                                                    posBottomLeft = g
                                                    cleanTiles7.remove(g)
                                                    for xg in range(4):
                                                        posBottomLeft = rotate(posBottomLeft)

                                                        for h in cleanTiles7:
                                                            game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                                                            if checkVertical(0) == False:
                                                                break
                                                            cleanTiles8 = cleanTiles7.copy()
                                                            posBottomCenter = h
                                                            cleanTiles8.remove(h)
                                                            for xh in range(4):
                                                                posBottomCenter = rotate(posBottomCenter)

                                                                for i in cleanTiles8:
                                                                    game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                                                                    if checkVertical(1) == False:
                                                                        break
                                                                    posBottomRight = i
                                                                    for xi in range(4):
                                                                        posBottomRight = rotate(posBottomRight)

                                                                        game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                                                                        if checkHorizontal(2) == False:
                                                                            break
                                                                        if checkVertical(2) == False:
                                                                            break
                                                                        if checkOblique(9) == False:
                                                                            break
                                                                        if checkRotate(sol9List) == False:
                                                                            break
                                                                        sol9Found += 1
                                                                        sol9List.append(game)

print("\nSolutions (x4) :")
for x in sol4List:
    printM(x)
print("\nSolutions (x6) :")
for x in sol6List:
    printM(x)
print("\nSolutions (x9) :")
for x in sol9List:
    printM(x)
print("\nFound (x4) : " + str(sol4Found) + "/32")
print("\nFound (x6) : " + str(sol6Found) + "/6")
print("\nFound (x9) : " + str(sol9Found) + "/2\n")
