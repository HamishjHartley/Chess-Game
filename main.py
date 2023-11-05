import numpy as np

from Peice import Peice
from Pawn import Pawn
from Bishop import Bishop
from Knight import Knight
from Rook import Rook

from Board import Board

#TODO: possibly create Move class, or move this to Board class
move_stack =[]

play_board = Board() 

# pawn1 = Pawn(1)    
# pawn2 = Pawn(1) 

# pawn3 = Pawn(1) 
# pawn4 = Pawn(1) 

bishop1 = Bishop(1) 
# knight1 = Knight(1) 

rook1 = Rook(1)

# play_board.add_peice(pawn2,5,3)
# play_board.add_peice(pawn1,6,2)
# play_board.add_peice(pawn4,6,4)
# play_board.add_peice(knight1,4,5)
play_board.add_peice(bishop1,5,4)
play_board.add_peice(rook1, 2,4)

#print(play_board.bit_board)

# print(pawn2.get_legal_moves())
#print(play_board.bit_board)
#print(rook1.get_legal_moves(play_board.bit_board))
print(bishop1.get_legal_moves(play_board.bit_board))


# print(pawn1.get_legal_moves())
# print(pawn2.get_legal_moves())