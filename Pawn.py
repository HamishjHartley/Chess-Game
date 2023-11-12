import numpy as np
from Peice import Peice

#Pawn class which is a child class of Peice
class Pawn(Peice):
    def __init__(self, colour:int):
        Peice.__init__(self, colour) #to keep the inheritance of Peice's "__init__" function
        #self.file_name = ["b_pawn.png", "w_pawn.png"]
        
        #Pawns movement rules
        self.straight_ahead = (self.v+1, self.h)
        self.capture_left = (self.v+1, self.h-1)
        self.capture_right = (self.v+1, self.h+1)

    def get_file_name(self):
        if self.COLOUR == -1:
            return "b_pawn.png"
        if self.COLOUR == 1:
            return "w_pawn.png"

    def check_legal_move(self,direction: tuple,bit_board):
        if bit_board[direction] == 0:
            self.legal_moves.append(direction)
            print(direction)
        elif bit_board[direction] == self.COLOUR * -1: #if inverse of current peice's colour
            print(direction)
            self.legal_moves.append(direction)

    #Returns a list of legal move(s) specific to a Pawn peice
    def get_legal_moves(self, bit_board):
        self.check_legal_move(self.straight_ahead,bit_board)
        #self.check_legal_move(self.capture_left,bit_board)
        #self.check_legal_move(self.capture_right,bit_board)

        return self.legal_moves