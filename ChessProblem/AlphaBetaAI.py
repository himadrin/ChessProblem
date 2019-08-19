#Himadri Naraimhamurthy
#AlphaBetaAI.py
#jan 24, 2019

import chess
from math import inf
from Heuristics import *


class AlphaBetaAI():
    def __init__(self, max_depth, depth=0):
        #this initializes the current depth for AB search
        self.depth = depth
        self.max_depth = max_depth

    # calls the final iteration of AB search determining move
    def choose_move(self, board, depth_limit=100):
        v = 0

        # call applyMinimax within the depth range
        for depth in range(depth_limit):
            move = self.applyAB(self.max_depth, board, True)
            v = v + 1

            if move != None:
                return move

    #uses ab search value to determine best move - iterative deepening
    def applyAB(self, depth, board, max_t):

        # get all possible moves and set extremes
        possibleMoves = board.legal_moves
        best_val = -10000
        al = -100000
        be = 100000
        best = None

        # run ab search and compare it with best_val to determine best node
        for m in possibleMoves:
            move = chess.Move.from_uci(str(m))

            # adds each move onto the stack in order to avoid creating new objects
            board.push(move)
            m_val = max(best_val, self.ab(depth - 1, board, al, be, not max_t))
            board.pop()

            if m_val>best_val:
                best_val = m_val
                best = m

        print("AlphaBeta ran " + str(self.depth) + " times!")
        return best

    # ab algorithm to get values of board
    def ab(self, max_depth, board, alpha, beta, max_tf):
        # recursive function updates depth count each time!
        self.depth = self.depth + 1
        move_list = board.legal_moves

        #exit for recursion - returns eval
        if self.cutoff_test(board, max_depth):
            return -1*getMaterialValue(board)

        #in case of maximizing - set extremes
        if (max_tf):
            max_move_val = -10000
            for m in move_list:
                move = chess.Move.from_uci(str(m))
                board.push(move)
                #recursive call to maximize value
                max_move_val = max(max_move_val, self.ab(max_depth - 1, board, alpha, beta, not max_tf))
                board.pop()

                # have the max val and set as alpha
                alpha = max(alpha, max_move_val)

            return alpha

        #in case of minimizing - set extremes
        else:
            min_move_val = 10000
            for m in move_list:
                move = chess.Move.from_uci(str(m))
                board.push(move)
                #recursive call to minimize value
                min_move_val = min(min_move_val, self.ab(max_depth - 1, board, alpha, beta, not max_tf))
                board.pop()

                #have the min value and set as beta
                beta = min(beta, min_move_val)

            return beta

    # cutoff test returns true if we are at max depth or if we are at
    # a draw or check or some closing state
    def cutoff_test(self, board, max_depth):
        if max_depth == 0:
            return True
        if max_depth != 0 and board.is_game_over():
            return True
        else:
            return False
