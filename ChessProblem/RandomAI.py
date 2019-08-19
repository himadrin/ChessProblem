#import chess
import random
from time import sleep
from Heuristics import *

class RandomAI():
    def __init__(self):
        pass

    def choose_move(self, board):
        moves = list(board.legal_moves)
        move = random.choice(moves)

        #test of heuristic
        print(getMaterialValue(board))

        sleep(1)   # I'm thinking so hard.
        print("Random AI recommending move " + str(move))
        return move
