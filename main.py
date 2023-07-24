# Vide = 0
# Bleu = 1
# Gris = 2
# Rose = 3
# Vert = 4
# Rouge = 5
# Jaune = 6

tile1 = [[5,6],
         [3,5]]

tile2 = [[2,4],
         [1,2]]

tile3 = [[2,6],
         [1,4]]

tile4 = [[1,4],
         [6,3]]

tile5 = [[4,6],
         [5,3]]

tile6 = [[3,1],
         [6,5]]

tile7 = [[2,4],
         [5,3]]

tile8 = [[3,2],
         [1,4]]

tile9 = [[5,1],
         [2,6]]

tiles = [tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9]

def rotateT(tile):
    res = [[0,0],
           [0,0]]
    res[0][0] = tile[1][0]
    res[0][1] = tile[0][0]
    res[1][0] = tile[1][1]
    res[1][1] = tile[0][1]
    return res

def rotateG(game):
    l1c1 = game[0][0][0][0]
    l1c2 = game[0][0][0][1]
    l1c3 = game[0][1][0][0]
    l1c4 = game[0][1][0][1]
    l1c5 = game[0][2][0][0]
    l1c6 = game[0][2][0][1]
    l2c1 = game[0][0][1][0]
    l2c2 = game[0][0][1][1]
    l2c3 = game[0][1][1][0]
    l2c4 = game[0][1][1][1]
    l2c5 = game[0][2][1][0]
    l2c6 = game[0][2][1][1]
    l3c1 = game[1][0][0][0]
    l3c2 = game[1][0][0][1]
    l3c3 = game[1][1][0][0]
    l3c4 = game[1][1][0][1]
    l3c5 = game[1][2][0][0]
    l3c6 = game[1][2][0][1]
    l4c1 = game[1][0][1][0]
    l4c2 = game[1][0][1][1]
    l4c3 = game[1][1][1][0]
    l4c4 = game[1][1][1][1]
    l4c5 = game[1][2][1][0]
    l4c6 = game[1][2][1][1]
    l5c1 = game[2][0][0][0]
    l5c2 = game[2][0][0][1]
    l5c3 = game[2][1][0][0]
    l5c4 = game[2][1][0][1]
    l5c5 = game[2][2][0][0]
    l5c6 = game[2][2][0][1]
    l6c1 = game[2][0][1][0]
    l6c2 = game[2][0][1][1]
    l6c3 = game[2][1][1][0]
    l6c4 = game[2][1][1][1]
    l6c5 = game[2][2][1][0]
    l6c6 = game[2][2][1][1]

    res = [[[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]]],[[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]]],[[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]]]]

    res[0][0][0][0] = l6c1
    res[0][0][0][1] = l5c1
    res[0][1][0][0] = l4c1
    res[0][1][0][1] = l3c1
    res[0][2][0][0] = l2c1
    res[0][2][0][1] = l1c1
    res[0][0][1][0] = l6c2
    res[0][0][1][1] = l5c2
    res[0][1][1][0] = l4c2
    res[0][1][1][1] = l3c2
    res[0][2][1][0] = l2c2
    res[0][2][1][1] = l1c2
    res[1][0][0][0] = l6c3
    res[1][0][0][1] = l5c3
    res[1][1][0][0] = l4c3
    res[1][1][0][1] = l3c3
    res[1][2][0][0] = l2c3
    res[1][2][0][1] = l1c3
    res[1][0][1][0] = l6c4
    res[1][0][1][1] = l5c4
    res[1][1][1][0] = l4c4
    res[1][1][1][1] = l3c4
    res[1][2][1][0] = l2c4
    res[1][2][1][1] = l1c4
    res[2][0][0][0] = l6c5
    res[2][0][0][1] = l5c5
    res[2][1][0][0] = l4c5
    res[2][1][0][1] = l3c5
    res[2][2][0][0] = l2c5
    res[2][2][0][1] = l1c5
    res[2][0][1][0] = l6c6
    res[2][0][1][1] = l5c6
    res[2][1][1][0] = l4c6
    res[2][1][1][1] = l3c6
    res[2][2][1][0] = l2c6
    res[2][2][1][1] = l1c6

    return res

def printT(tile):
    print(color(tile[0][0]) + color(tile[0][1]) + "\n" +
          color(tile[1][0]) + color(tile[1][1]) + "\n")

def printG(game):
    print(color(game[0][0][0][0]) + color(game[0][0][0][1]) + color(game[0][1][0][0]) + color(game[0][1][0][1]) + color(game[0][2][0][0]) + color(game[0][2][0][1]) + "\n" +
          color(game[0][0][1][0]) + color(game[0][0][1][1]) + color(game[0][1][1][0]) + color(game[0][1][1][1]) + color(game[0][2][1][0]) + color(game[0][2][1][1]) + "\n" +
          color(game[1][0][0][0]) + color(game[1][0][0][1]) + color(game[1][1][0][0]) + color(game[1][1][0][1]) + color(game[1][2][0][0]) + color(game[1][2][0][1]) + "\n" +
          color(game[1][0][1][0]) + color(game[1][0][1][1]) + color(game[1][1][1][0]) + color(game[1][1][1][1]) + color(game[1][2][1][0]) + color(game[1][2][1][1]) + "\n" +
          color(game[2][0][0][0]) + color(game[2][0][0][1]) + color(game[2][1][0][0]) + color(game[2][1][0][1]) + color(game[2][2][0][0]) + color(game[2][2][0][1]) + "\n" +
          color(game[2][0][1][0]) + color(game[2][0][1][1]) + color(game[2][1][1][0]) + color(game[2][1][1][1]) + color(game[2][2][1][0]) + color(game[2][2][1][1]) + "\n")

def checkHorizontal(game,line):
    if line == 1:
        line1 = [game[0][0][0][0],game[0][0][0][1],game[0][1][0][0],game[0][1][0][1],game[0][2][0][0],game[0][2][0][1]]
        line2 = [game[0][0][1][0],game[0][0][1][1],game[0][1][1][0],game[0][1][1][1],game[0][2][1][0],game[0][2][1][1]]
        
        while len(line1) != 1:
            if line1[0] != 0 and line1[0] in line1[1:]:
                return False
            line1 = line1[1:]
        
        while len(line2) != 1:
            if line2[0] != 0 and line2[0] in line2[1:]:
                return False
            line2 = line2[1:]

    elif line == 2:
        line3 = [game[1][0][0][0],game[1][0][0][1],game[1][1][0][0],game[1][1][0][1],game[1][2][0][0],game[1][2][0][1]]
        line4 = [game[1][0][1][0],game[1][0][1][1],game[1][1][1][0],game[1][1][1][1],game[1][2][1][0],game[1][2][1][1]]
        
        while len(line3) != 1:
            if line3[0] != 0 and line3[0] in line3[1:]:
                return False
            line3 = line3[1:]
        
        while len(line4) != 1:
            if line4[0] != 0 and line4[0] in line4[1:]:
                return False
            line4 = line4[1:]

    elif line == 3:
        line5 = [game[2][0][0][0],game[2][0][0][1],game[2][1][0][0],game[2][1][0][1],game[2][2][0][0],game[2][2][0][1]]
        line6 = [game[2][0][1][0],game[2][0][1][1],game[2][1][1][0],game[2][1][1][1],game[2][2][1][0],game[2][2][1][1]]
        
        while len(line5) != 1:
            if line5[0] != 0 and line5[0] in line5[1:]:
                return False
            line5 = line5[1:]
        
        while len(line6) != 1:
            if line6[0] != 0 and line6[0] in line6[1:]:
                return False
            line6 = line6[1:]
    
    return True

def checkVertical(game,col):
    if col == 1:
        col1 = [game[0][0][0][0],game[0][0][1][0],game[1][0][0][0],game[1][0][1][0],game[2][0][0][0],game[2][0][1][0]]
        col2 = [game[0][0][0][1],game[0][0][1][1],game[1][0][0][1],game[1][0][1][1],game[2][0][0][1],game[2][0][1][1]]

        while len(col1) != 1:
            if col1[0] != 0 and col1[0] in col1[1:]:
                return False
            col1 = col1[1:]
        
        while len(col2) != 1:
            if col2[0] != 0 and col2[0] in col2[1:]:
                return False
            col2 = col2[1:]
    
    elif col == 2:
        col3 = [game[0][1][0][0],game[0][1][1][0],game[1][1][0][0],game[1][1][1][0],game[2][1][0][0],game[2][1][1][0]]
        col4 = [game[0][1][0][1],game[0][1][1][1],game[1][1][0][1],game[1][1][1][1],game[2][1][0][1],game[2][1][1][1]]
        
        while len(col3) != 1:
            if col3[0] != 0 and col3[0] in col3[1:]:
                return False
            col3 = col3[1:]
        
        while len(col4) != 1:
            if col4[0] != 0 and col4[0] in col4[1:]:
                return False
            col4 = col4[1:]
    
    elif col == 3:
        col5 = [game[0][2][0][0],game[0][2][1][0],game[1][2][0][0],game[1][2][1][0],game[2][2][0][0],game[2][2][1][0]]
        col6 = [game[0][2][0][1],game[0][2][1][1],game[1][2][0][1],game[1][2][1][1],game[2][2][0][1],game[2][2][1][1]]
        
        while len(col5) != 1:
            if col5[0] != 0 and col5[0] in col5[1:]:
                return False
            col5 = col5[1:]
        
        while len(col6) != 1:
            if col6[0] != 0 and col6[0] in col6[1:]:
                return False
            col6 = col6[1:]
    
    return True

def checkOblique(game,cards):
    if cards == 4:
        obl1 = [game[0][0][0][0],game[0][0][1][1],game[1][1][0][0],game[1][1][1][1]]
        obl2 = [game[1][0][1][0],game[1][0][0][1],game[0][1][1][0],game[0][1][0][1]]

        while len(obl1) != 1:
            if obl1[0] != 0 and obl1[0] in obl1[1:]:
                return False
            obl1 = obl1[1:]
        
        while len(obl2) != 1:
            if obl2[0] != 0 and obl2[0] in obl2[1:]:
                return False
            obl2 = obl2[1:]
    
    elif cards == 6:
        obl3 = [game[0][0][0][0],game[0][0][1][1],game[1][1][0][0],game[1][1][1][1]]
        obl4 = [game[0][1][0][0],game[0][1][1][1],game[1][2][0][0],game[1][2][1][1]]
        obl5 = [game[1][0][1][0],game[1][0][0][1],game[0][1][1][0],game[0][1][0][1]]
        obl6 = [game[1][1][1][0],game[1][1][0][1],game[0][2][1][0],game[0][2][0][1]]

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
        obl7 = [game[0][0][0][0],game[0][0][1][1],game[1][1][0][0],game[1][1][1][1],game[2][2][0][0],game[2][2][1][1]]
        obl8 = [game[2][0][1][0],game[2][0][0][1],game[1][1][1][0],game[1][1][0][1],game[0][2][1][0],game[0][2][0][1]]

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
            return "'"

if __name__ == "__main__":

    print("Tiles and game :\n")

    for x in tiles:
        printT(x)

    game = [[tile1,tile2,tile3],[tile4,tile5,tile6],[tile7,tile8,tile9]]
    printG(game)

    print("Solutions avec 4 pièces :\n")

    listSol = []
    found = 0

    posUpLeft = [[0,0],
                 [0,0]]
    posUpCenter = [[0,0],
                   [0,0]]
    posUpRight = [[0,0],
                  [0,0]]
    posMiddleLeft = [[0,0],
                     [0,0]]
    posMiddleCenter = [[0,0],
                       [0,0]]
    posMiddleRight = [[0,0],
                      [0,0]]
    posBottomLeft = [[0,0],
                     [0,0]]
    posBottomCenter = [[0,0],
                       [0,0]]
    posBottomRight = [[0,0],
                      [0,0]]
    game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]

    for a in tiles:
        cleanTiles1 = tiles.copy()
        posUpLeft = a
        cleanTiles1.remove(a)
        for b in range(4):
            posUpLeft = rotateT(posUpLeft)

            for c in cleanTiles1:
                cleanTiles2 = cleanTiles1.copy()
                posUpCenter = c
                cleanTiles2.remove(c)
                for d in range(4):
                    posUpCenter = rotateT(posUpCenter)

                    for e in cleanTiles2:
                        game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                        if checkHorizontal(game,1) == False:
                            break
                        cleanTiles3 = cleanTiles2.copy()
                        posMiddleLeft = e
                        cleanTiles3.remove(e)
                        for f in range(4):
                            posMiddleLeft = rotateT(posMiddleLeft)

                            for g in cleanTiles3:
                                game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                                if checkVertical(game,1) == False:
                                    break
                                posMiddleCenter = g
                                for h in range(4):
                                    posMiddleCenter = rotateT(posMiddleCenter)

                                    game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                                    if checkHorizontal(game,2) == False:
                                        break
                                    if checkVertical(game,2) == False:
                                        break
                                    if checkOblique(game,4) == False:
                                        break
                                    for i in range(4):
                                        check = True
                                        test = rotateG(game)
                                        if test in listSol:
                                            check = False
                                            break
                                    if check == False:
                                        break
                                    found += 1
                                    printG(game)
                                    listSol.append(game)

    print("Found : " + str(found) + "/32\n")

    print("Solutions avec 6 pièces :\n")

    listSol = []
    found = 0

    posUpLeft = [[0,0],
                 [0,0]]
    posUpCenter = [[0,0],
                   [0,0]]
    posUpRight = [[0,0],
                  [0,0]]
    posMiddleLeft = [[0,0],
                     [0,0]]
    posMiddleCenter = [[0,0],
                       [0,0]]
    posMiddleRight = [[0,0],
                      [0,0]]
    posBottomLeft = [[0,0],
                     [0,0]]
    posBottomCenter = [[0,0],
                       [0,0]]
    posBottomRight = [[0,0],
                      [0,0]]
    game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]

    for a in tiles:
        cleanTiles1 = tiles.copy()
        posUpLeft = a
        cleanTiles1.remove(a)
        for b in range(4):
            posUpLeft = rotateT(posUpLeft)

            for c in cleanTiles1:
                cleanTiles2 = cleanTiles1.copy()
                posUpCenter = c
                cleanTiles2.remove(c)
                for d in range(4):
                    posUpCenter = rotateT(posUpCenter)

                    for e in cleanTiles2:
                        cleanTiles3 = cleanTiles2.copy()
                        posUpRight = e
                        cleanTiles3.remove(e)
                        for f in range(4):
                            posUpRight = rotateT(posUpRight)

                            for g in cleanTiles3:
                                game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                                if checkHorizontal(game,1) == False:
                                    break
                                cleanTiles4 = cleanTiles3.copy()
                                posMiddleLeft = g
                                cleanTiles4.remove(g)
                                for h in range(4):
                                    posMiddleLeft = rotateT(posMiddleLeft)

                                    for i in cleanTiles4:
                                        game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                                        if checkVertical(game,1) == False:
                                            break
                                        cleanTiles5 = cleanTiles4.copy()
                                        posMiddleCenter = i
                                        cleanTiles5.remove(i)
                                        for j in range(4):
                                            posMiddleCenter = rotateT(posMiddleCenter)

                                            for k in cleanTiles5:
                                                game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                                                if checkVertical(game,2) == False:
                                                    break
                                                posMiddleRight = k
                                                for l in range(4):
                                                    posMiddleRight = rotateT(posMiddleRight)

                                                    game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                                                    if checkHorizontal(game,2) == False:
                                                        break
                                                    if checkVertical(game,3) == False:
                                                        break
                                                    if checkOblique(game,6) == False:
                                                        break
                                                    for i in range(4):
                                                        check = True
                                                        test = rotateG(game)
                                                        if test in listSol:
                                                            check = False
                                                            break
                                                    if check == False:
                                                        break
                                                    found += 1
                                                    printG(game)
                                                    listSol.append(game)

    print("Found : " + str(found) + "/6\n")
    
    print("Solutions avec 9 pièces :\n")

    listSol = []
    found = 0

    posUpLeft = [[0,0],
                 [0,0]]
    posUpCenter = [[0,0],
                   [0,0]]
    posUpRight = [[0,0],
                  [0,0]]
    posMiddleLeft = [[0,0],
                     [0,0]]
    posMiddleCenter = [[0,0],
                       [0,0]]
    posMiddleRight = [[0,0],
                      [0,0]]
    posBottomLeft = [[0,0],
                     [0,0]]
    posBottomCenter = [[0,0],
                       [0,0]]
    posBottomRight = [[0,0],
                      [0,0]]
    game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]

    for a in tiles:
        cleanTiles1 = tiles.copy()
        posUpLeft = a
        cleanTiles1.remove(a)
        for b in range(4):
            posUpLeft = rotateT(posUpLeft)

            for c in cleanTiles1:
                cleanTiles2 = cleanTiles1.copy()
                posUpCenter = c
                cleanTiles2.remove(c)
                for d in range(4):
                    posUpCenter = rotateT(posUpCenter)

                    for e in cleanTiles2:
                        cleanTiles3 = cleanTiles2.copy()
                        posUpRight = e
                        cleanTiles3.remove(e)
                        for f in range(4):
                            posUpRight = rotateT(posUpRight)

                            for g in cleanTiles3:
                                game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                                if checkHorizontal(game,1) == False:
                                    break
                                cleanTiles4 = cleanTiles3.copy()
                                posMiddleLeft = g
                                cleanTiles4.remove(g)
                                for h in range(4):
                                    posMiddleLeft = rotateT(posMiddleLeft)

                                    for i in cleanTiles4:
                                        cleanTiles5 = cleanTiles4.copy()
                                        posMiddleCenter = i
                                        cleanTiles5.remove(i)
                                        for j in range(4):
                                            posMiddleCenter = rotateT(posMiddleCenter)

                                            for k in cleanTiles5:
                                                cleanTiles6 = cleanTiles5.copy()
                                                posMiddleRight = k
                                                cleanTiles6.remove(k)
                                                for l in range(4):
                                                    posMiddleRight = rotateT(posMiddleRight)

                                                    for m in cleanTiles6:
                                                        game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                                                        if checkHorizontal(game,2) == False:
                                                            break
                                                        cleanTiles7 = cleanTiles6.copy()
                                                        posBottomLeft = m
                                                        cleanTiles7.remove(m)
                                                        for n in range(4):
                                                            posBottomLeft = rotateT(posBottomLeft)

                                                            for o in cleanTiles7:
                                                                game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                                                                if checkVertical(game,1) == False:
                                                                    break
                                                                cleanTiles8 = cleanTiles7.copy()
                                                                posBottomCenter = o
                                                                cleanTiles8.remove(o)
                                                                for p in range(4):
                                                                    posBottomCenter = rotateT(posBottomCenter)

                                                                    for q in cleanTiles8:
                                                                        game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                                                                        if checkVertical(game,2) == False:
                                                                            break
                                                                        posBottomRight = q
                                                                        for r in range(4):
                                                                            posBottomRight = rotateT(posBottomRight)

                                                                            game = [[posUpLeft,posUpCenter,posUpRight],[posMiddleLeft,posMiddleCenter,posMiddleRight],[posBottomLeft,posBottomCenter,posBottomRight]]
                                                                            if checkHorizontal(game,3) == False:
                                                                                break
                                                                            if checkVertical(game,3) == False:
                                                                                break
                                                                            if checkOblique(game,9) == False:
                                                                                break
                                                                            for i in range(4):
                                                                                check = True
                                                                                test = rotateG(game)
                                                                                if test in listSol:
                                                                                    check = False
                                                                                    break
                                                                            if check == False:
                                                                                break
                                                                            found += 1
                                                                            printG(game)
                                                                            listSol.append(game)

    print("Found : " + str(found) + "/2\n")