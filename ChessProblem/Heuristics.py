#Himadri Narasimhamurthy
#1/24/2019
#Includes material heuristic functions used in the AIs

#Material Value Heuristic Helper
#depending on the piece selected - returns the material value
#values are from the text - king assumed to be 0 since king is goal
def getPieceValue(p):
    value = 0

    if (p == None):
        return 0
    if p == "p" or p == "P":
        value = 1
    if p == "n" or p == "N" or p == "b" or p == "B":
        value = 3
    if p == "r" or p == "R":
        value = 5
    if p == "q" or p == "Q":
        value = 9
    if p == "k" or p == "K":
        value = 0

    return value

#getting total board value
def getMaterialValue(board):
    i = 1
    total = 0
    #number from python-chess documentation
    while i < 63:
        if board.piece_at(i) is not None:
            #if white - then we add positive value
            if bool(board.piece_at(i).color):
                add = getPieceValue(str(board.piece_at(i)))

            #if black we add a negative value
            else:
                add = -1*getPieceValue(str(board.piece_at(i)))
            total = total + add

        i = i+ 1
    return total

