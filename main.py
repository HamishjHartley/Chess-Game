import numpy as np

import Peice
import Pawn
import Bishop
import Knight
import Rook
import Board

#TODO: possibly create Move class, or move this to Board class
move_stack =[]

play_board = Board() 

pawn1 = Pawn(1) #White pawn    
pawn2 = Pawn(1) #White pawn

pawn3 = Pawn(1) #Black pawn
pawn4 = Pawn(1) #Black pawn

bishop1 = Bishop(1) #White bishop
knight1 = Knight(1) #White knight

play_board.add_peice(pawn2,5,3)
play_board.add_peice(pawn1,6,2)
play_board.add_peice(pawn4,6,4)
play_board.add_peice(knight1,0,0)

#print(play_board.bit_board)

# print(pawn2.get_legal_moves())
print(knight1.get_legal_moves())


# print(pawn1.get_legal_moves())
# print(pawn2.get_legal_moves())