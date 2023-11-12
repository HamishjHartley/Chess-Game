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

    def check_legal_move(self,v:int,h:int,bit_board,capture:bool):
        if bit_board[v,h] == 0 and capture ==False:
            self.legal_moves.append((v,h))
            print(v,h)
        elif bit_board[v,h] == self.COLOUR * -1 and capture == True: #if inverse of current peice's colour
            print(v,h)
            self.legal_moves.append((v,h))

    #Returns a list of legal move(s) specific to a Pawn peice
    def get_legal_moves(self, bit_board):
        #White pawn forward movement
        if self.COLOUR == 1:
            #Straight ahead
            self.check_legal_move(self.v+1, self.h,bit_board,False)
            #Capture left
            self.check_legal_move(self.v+1, self.h-1,bit_board,True)
            #Capture right
            self.check_legal_move(self.v+1, self.h+1,bit_board,True)
        #Black pawn forward movement
        elif self.COLOUR == -1:
            #Straight ahead
            self.check_legal_move(self.v-1, self.h,bit_board,False)
            #Capture left
            self.check_legal_move(self.v-1, self.h+1,bit_board,True)
            #Capture right
            self.check_legal_move(self.v-1, self.h-1,bit_board,True)

        return self.legal_moves