import numpy as np
from Peice import Peice

#Pawn class which is a child class of Peice
class Pawn(Peice):
    def __init__(self, colour:int):
        Peice.__init__(self, colour) #to keep the inheritance of Peice's "__init__" function


    #Returns a list of legal move(s) specific to a Pawn peice
    def get_legal_moves(self, bit_board):
        #Pawns movement rules
        straight_ahead = (self.v+1, self.h)
        capture_left = (self.v+1, self.h-1)
        capture_right = (self.v+1, self.h+1)

        board_state = bit_board #Copies board state from bit board

        #Straight ahead
        if board_state[straight_ahead] == 0:
            self.legal_moves.append(straight_ahead)
        elif board_state[straight_ahead] == self.COLOUR * -1: #if inverse of current peice's colour
            self.legal_moves.append(straight_ahead)
        
        #Capture left
        if board_state[capture_left] == 0:
            self.legal_moves.append(capture_left)
        elif board_state[capture_left] == self.COLOUR * -1: #if inverse of current peice's colour
            self.legal_moves.append(capture_left)

        #Capture right
        if board_state[capture_right] == 0:
            self.legal_moves.append(capture_right)
        elif board_state[capture_right] == self.COLOUR * -1: #if inverse of current peice's colour
            self.legal_moves.append(capture_right)

        return self.legal_moves