import numpy as np
from Peice import Peice
from Board import Board

#Knight class which is a child class of Peice
class Knight(Peice):
    def __init__(self, colour):
        Peice.__init__(self, colour) #to keep the inheritance of Peice's "__init__" function

    def get_legal_moves(self,bit_board):
        possible_moves =[(1,-2), (2,-1),(2,1),(1,2),(-1,-2),(-2,-1),(-2,1),(-1,2)] #8 Possible squares knight can hop to, relative to current square

        board_state = bit_board

        for i in range(len(possible_moves)):
            if board_state[self.v + possible_moves[i][0],self.h + possible_moves[i][1]] == self.COLOUR *-1: #if square has opposite coloured peice
                self.legal_moves.append((self.v + possible_moves[i][0],self.h + possible_moves[i][1]))
                board_state[self.v + possible_moves[i][0],self.h + possible_moves[i][1]] = 9

            if board_state[self.v + possible_moves[i][0],self.h + possible_moves[i][1]] == 0: #if square is empty
                self.legal_moves.append((self.v + possible_moves[i][0],self.h + possible_moves[i][1]))
                board_state[self.v + possible_moves[i][0],self.h + possible_moves[i][1]] = 9

            # print(board_state[self.v + possible_moves[i][0],self.h + possible_moves[i][1]])
            # print("\n")
            # print(self.v + possible_moves[i][0])
            # print(self.h + possible_moves[i][1])
            i +=1
        return self.legal_moves