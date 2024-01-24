# Vide = 0
# Bleu = 1
# Gris = 2
# Rose = 3
# Vert = 4
# Rouge = 5
# Jaune = 6

tile1 = [(5, 6),
         (3, 5)]

tile2 = [(2, 4),
         (1, 2)]

tile3 = [(2, 6),
         (1, 4)]

tile4 = [(1, 4),
         (6, 3)]

tile5 = [(4, 6),
         (5, 3)]

tile6 = [(3, 1),
         (6, 5)]

tile7 = [(2, 4),
         (5, 3)]

tile8 = [(3, 2),
         (1, 4)]

tile9 = [(5, 1),
         (2, 6)]

tile0 = [(0, 0),
         (0, 0)]

tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9]


def rotate(matrix):
    try:
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                matrix[x][y] = rotate(matrix[x][y])
    finally:
        return list(zip(*matrix[::-1]))


def printT(matrix):
    for a in range(2):
        for b in range(2):
            print(color(matrix[a][b]), end="")
        print("")
    print("")


def printM(matrix):
    for a in range(3):
        for b in range(2):
            for c in range(3):
                for d in range(2):
                    print(color(matrix[a][c][b][d]), end="")
            print("")
    print("")


def checkHorizontal(game, line):
    if line == 1:
        line1 = [game[0][0][0][0], game[0][0][0][1], game[0][1][0][0], game[0][1][0][1], game[0][2][0][0], game[0][2][0][1]]
        line2 = [game[0][0][1][0], game[0][0][1][1], game[0][1][1][0], game[0][1][1][1], game[0][2][1][0], game[0][2][1][1]]

        while len(line1) != 1:
            if line1[0] != 0 and line1[0] in line1[1:]:
                return False
            line1 = line1[1:]

        while len(line2) != 1:
            if line2[0] != 0 and line2[0] in line2[1:]:
                return False
            line2 = line2[1:]

    elif line == 2:
        line3 = [game[1][0][0][0], game[1][0][0][1], game[1][1][0][0], game[1][1][0][1], game[1][2][0][0], game[1][2][0][1]]
        line4 = [game[1][0][1][0], game[1][0][1][1], game[1][1][1][0], game[1][1][1][1], game[1][2][1][0], game[1][2][1][1]]

        while len(line3) != 1:
            if line3[0] != 0 and line3[0] in line3[1:]:
                return False
            line3 = line3[1:]

        while len(line4) != 1:
            if line4[0] != 0 and line4[0] in line4[1:]:
                return False
            line4 = line4[1:]

    elif line == 3:
        line5 = [game[2][0][0][0], game[2][0][0][1], game[2][1][0][0], game[2][1][0][1], game[2][2][0][0], game[2][2][0][1]]
        line6 = [game[2][0][1][0], game[2][0][1][1], game[2][1][1][0], game[2][1][1][1], game[2][2][1][0], game[2][2][1][1]]

        while len(line5) != 1:
            if line5[0] != 0 and line5[0] in line5[1:]:
                return False
            line5 = line5[1:]

        while len(line6) != 1:
            if line6[0] != 0 and line6[0] in line6[1:]:
                return False
            line6 = line6[1:]

    return True


def checkVertical(game, col):
    if col == 1:
        col1 = [game[0][0][0][0], game[0][0][1][0], game[1][0][0][0], game[1][0][1][0], game[2][0][0][0], game[2][0][1][0]]
        col2 = [game[0][0][0][1], game[0][0][1][1], game[1][0][0][1], game[1][0][1][1], game[2][0][0][1], game[2][0][1][1]]

        while len(col1) != 1:
            if col1[0] != 0 and col1[0] in col1[1:]:
                return False
            col1 = col1[1:]

        while len(col2) != 1:
            if col2[0] != 0 and col2[0] in col2[1:]:
                return False
            col2 = col2[1:]

    elif col == 2:
        col3 = [game[0][1][0][0], game[0][1][1][0], game[1][1][0][0], game[1][1][1][0], game[2][1][0][0], game[2][1][1][0]]
        col4 = [game[0][1][0][1], game[0][1][1][1], game[1][1][0][1], game[1][1][1][1], game[2][1][0][1], game[2][1][1][1]]

        while len(col3) != 1:
            if col3[0] != 0 and col3[0] in col3[1:]:
                return False
            col3 = col3[1:]

        while len(col4) != 1:
            if col4[0] != 0 and col4[0] in col4[1:]:
                return False
            col4 = col4[1:]

    elif col == 3:
        col5 = [game[0][2][0][0], game[0][2][1][0], game[1][2][0][0], game[1][2][1][0], game[2][2][0][0], game[2][2][1][0]]
        col6 = [game[0][2][0][1], game[0][2][1][1], game[1][2][0][1], game[1][2][1][1], game[2][2][0][1], game[2][2][1][1]]

        while len(col5) != 1:
            if col5[0] != 0 and col5[0] in col5[1:]:
                return False
            col5 = col5[1:]

        while len(col6) != 1:
            if col6[0] != 0 and col6[0] in col6[1:]:
                return False
            col6 = col6[1:]

    return True


def checkOblique(game, cards):
    if cards == 4:
        obl1 = [game[0][0][0][0], game[0][0][1][1], game[1][1][0][0], game[1][1][1][1]]
        obl2 = [game[1][0][1][0], game[1][0][0][1], game[0][1][1][0], game[0][1][0][1]]

        while len(obl1) != 1:
            if obl1[0] != 0 and obl1[0] in obl1[1:]:
                return False
            obl1 = obl1[1:]

        while len(obl2) != 1:
            if obl2[0] != 0 and obl2[0] in obl2[1:]:
                return False
            obl2 = obl2[1:]

    elif cards == 6:
        obl3 = [game[0][0][0][0], game[0][0][1][1], game[1][1][0][0], game[1][1][1][1]]
        obl4 = [game[0][1][0][0], game[0][1][1][1], game[1][2][0][0], game[1][2][1][1]]
        obl5 = [game[1][0][1][0], game[1][0][0][1], game[0][1][1][0], game[0][1][0][1]]
        obl6 = [game[1][1][1][0], game[1][1][0][1], game[0][2][1][0], game[0][2][0][1]]

        while len(obl3) != 1:
            if obl3[0] != 0 and obl3[0] in obl3[1:]:
                return False
            obl3 = obl3[1:]

        while len(obl4) != 1:
            if obl4[0] != 0 and obl4[0] in obl4[1:]:
                return False
            obl4 = obl4[1:]

        while len(obl5) != 1:
            if obl5[0] != 0 and obl5[0] in obl5[1:]:
                return False
            obl5 = obl5[1:]

        while len(obl6) != 1:
            if obl6[0] != 0 and obl6[0] in obl6[1:]:
                return False
            obl6 = obl6[1:]

    elif cards == 9:
        obl7 = [game[0][0][0][0], game[0][0][1][1], game[1][1][0][0], game[1][1][1][1], game[2][2][0][0], game[2][2][1][1]]
        obl8 = [game[2][0][1][0], game[2][0][0][1], game[1][1][1][0], game[1][1][0][1], game[0][2][1][0], game[0][2][0][1]]

        while len(obl7) != 1:
            if obl7[0] != 0 and obl7[0] in obl7[1:]:
                return False
            obl7 = obl7[1:]

        while len(obl8) != 1:
            if obl8[0] != 0 and obl8[0] in obl8[1:]:
                return False
            obl8 = obl8[1:]

    return True


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


print("Tiles :\n")

for x in tiles:
    printT(x)

game = [[tile1, tile2, tile3], [tile4, tile5, tile6], [tile7, tile8, tile9]]

sol4List = []
sol4Found = 0
sol6List = []
sol6Found = 0
sol9List = []
sol9Found = 0

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
                            if checkHorizontal(game, 1) == False:
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
                                                    if checkHorizontal(game, 2) == False:
                                                        break
                                                    cleanTiles7 = cleanTiles6.copy()
                                                    posBottomLeft = g
                                                    cleanTiles7.remove(g)
                                                    for xg in range(4):
                                                        posBottomLeft = rotate(posBottomLeft)

                                                        for h in cleanTiles7:
                                                            game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                                                            if checkVertical(game, 1) == False:
                                                                break
                                                            cleanTiles8 = cleanTiles7.copy()
                                                            posBottomCenter = h
                                                            cleanTiles8.remove(h)
                                                            for xh in range(4):
                                                                posBottomCenter = rotate(posBottomCenter)

                                                                for i in cleanTiles8:
                                                                    game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                                                                    if checkVertical(game, 2) == False:
                                                                        break
                                                                    posBottomRight = i
                                                                    for xi in range(4):
                                                                        posBottomRight = rotate(posBottomRight)

                                                                        game = [[posUpLeft, posUpCenter, posUpRight], [posMiddleLeft, posMiddleCenter, posMiddleRight], [posBottomLeft, posBottomCenter, posBottomRight]]
                                                                        if checkHorizontal(game, 3) == False:
                                                                            break
                                                                        if checkVertical(game, 3) == False:
                                                                            break
                                                                        if checkOblique(game, 9) == False:
                                                                            break
                                                                        for xxx in range(4):
                                                                            check = True
                                                                            test = rotate(game)
                                                                            if test in sol9List:
                                                                                check = False
                                                                                break
                                                                        if check == False:
                                                                            break
                                                                        sol9Found += 1
                                                                        sol9List.append(game)

print("Solutions (x4) :\n")
for x in sol4List:
    printM(x)
print("Solutions (x6) :\n")
for x in sol6List:
    printM(x)
print("Solutions (x9) :\n")
for x in sol9List:
    printM(x)
print("Found (x4) : " + str(sol4Found) + "/32\n")
print("Found (x6) : " + str(sol6Found) + "/6\n")
print("Found (x9) : " + str(sol9Found) + "/2\n")
