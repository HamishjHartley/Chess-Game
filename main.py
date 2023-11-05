import numpy as np
import copy

from Peice import Peice
from Pawn import Pawn
from Bishop import Bishop
from Knight import Knight
from Rook import Rook
from Queen import Queen
from King import King

from Board import Board

play_board = Board()

#Initializes game based on FEN code
def initalize_game(FEN):
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    board_row = FEN.split("/")
    for i in range (len(board_row)):
        if board_row[i] == 8:
            play_board[i, 0:7] ==0 #empty row
        else:
            char_list = []
            for letter in board_row[i]:
                char_list.append(letter)
            for j in range (len(char_list)):
                if char_list[j] == "r":
                    rook = copy.deepcopy(Rook(1)) 
                    play_board.add_peice(rook,board_row[i],j)
                if char_list[j] =="n":
                    knight = copy.deepcopy(Knight(1))
                    play_board.add_peice(knight,board_row[i],j)
                if char_list[j] == "b":
                    bishop = copy.deepcopy(Bishop(1))
                    play_board.add_peice(bishop, board_row[i],j)
                if char_list[j] =="q":
                    queen = copy.deepcopy(Queen(1))
                    play_board.add_peice(queen, board_row[i],j)
                if char_list[j] =="k":
                    king = copy.deepcopy(King(1))
                    play_board.add_peice(king, board_row[i],j)
                if char_list[j] =="p":
                    pawn = copy.deepcopy(Pawn(1))
    return FEN


# pawn1 = Pawn(1)    
# pawn2 = Pawn(1) 

# pawn3 = Pawn(1) 
# pawn4 = Pawn(1) 

bishop1 = Bishop(1) 
# knight1 = Knight(1) 

rook1 = Rook(1)
queen1 = Queen(1)
king1 = King(1)

# play_board.add_peice(pawn2,5,3)
# play_board.add_peice(pawn1,6,2)
# play_board.add_peice(pawn4,6,4)
# play_board.add_peice(knight1,4,5)
play_board.add_peice(bishop1,5,4)
play_board.add_peice(rook1, 2,4)
play_board.add_peice(queen1, 3,3)
play_board.add_peice(king1,5,5)

#print(play_board.bit_board)

# print(pawn2.get_legal_moves())
#print(play_board.bit_board)
#print(rook1.get_legal_moves(play_board.bit_board))
#print(queen1.get_legal_moves(play_board.bit_board))
print(king1.get_legal_moves(play_board.bit_board))



# print(pawn1.get_legal_moves())
# print(pawn2.get_legal_moves())