import numpy as np
from Peice import Peice

#Board class
#is the controller class to which "Peices" are added, handles events/interaction's between peices
class Board:
    #constructor to initialize 8x8 board array
    def __init__(self):
        self.board = np.zeros((8,8), dtype=Peice)

        #"bit board" to hold the state of each square on the board for easier move/capture calculation
        self.bit_board = np.zeros((8,8), dtype=int)

    #Adds a peice to a position on the 8x8 board array defined by index (pos)
    #TODO: Throw exception if position reference out of bounds of board array
    def add_peice(self, Peice, v, h):
        self.board[v,h]= Peice
        Peice.update_position(v, h)

        #Simulatniously update bit board with the associated integer value for each sqaure. 
        self.bit_board[v, h] = Peice.COLOUR

    #Removes a given peice from the 8x8 board array(By replacing with a 0)
    #TODO:Find a better way to do this
    def remove_peice(self, Peice):
        #np.delete(self.board, [Peice.currentPosition()])
        self.board[Peice.current_position()]= 0

        #Simulatniously updates bit board 
        self.bit_board[Peice.current_position()] = 0
    
    # #Moves a given peice to a target position
    #by removing from origional square and adding it to target square
    #TODO:Find better way to do this
    def move_peice(self, Peice, v, h):
        self.remove_peice(Peice)
        self.add_peice(Peice, v, h)

    def get_bit_board(self):
        return self.bit_board
