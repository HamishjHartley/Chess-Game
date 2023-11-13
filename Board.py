import numpy as np
from Peice import Peice

#Board class
#is the controller class to which "Peices" are added, handles events/interaction's between peices
class Board:
    #constructor to initialize 8x8 board array
    def __init__(self):
        self.board = np.zeros((8,8), dtype=Peice)

        #"bit board" to hold the state of each square on the board for easier move/capture calculation
        self.bit_board = np.full((8,8),0,dtype=int)

        #TODO: possibly create Move class, or move this to Board class
        move_stack =[]

    #Adds a peice to a position on the 8x8 board array defined by index (pos)
    #TODO: Throw exception if position reference out of bounds of board array
    def add_peice(self, Peice: Peice, v : int, h: int):
        self.board[v,h]= Peice
        #Simulatniously update bit board with the associated integer value for each sqaure. 
        #-1 for black, 1 for white
        if Peice.COLOUR == -1:
            self.bit_board[v, h] = -1
        if Peice.COLOUR == 1:
            self.bit_board[v, h] = 1
        Peice.update_position(v, h)

    #Removes a given peice from the 8x8 board array(By replacing with a 0)
    def remove_peice(self,v:int,h:int, Peice: Peice):
        self.board[v,h]=0

        #Simulatniously updates bit board 
        self.bit_board[v,h] = 0
    
    # #Moves a given peice to a target position
    #by removing from original square and adding it to target square
    def move_peice(self, Peice: Peice, v: int, h:int):
        self.remove_peice(Peice)
        self.add_peice(Peice, v, h)
     
 
    def get_bit_board(self):
        return self.bit_board