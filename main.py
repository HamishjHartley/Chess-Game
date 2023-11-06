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

from window2 import QS

play_board = Board()

#Initializes game based on FEN code
def initalize_from_fen(FEN):
    #Reverse FEN string
    fen = FEN [::-1]
    char_list = list(fen)

    row_index=0
    colum_index=0

    for char in char_list:
        peice = None 
        if char == "/":
            row_index +=1
            colum_index =0
            print("New line")
            continue # Go to next iteration and skip following code
        if char.isdigit() == True:
            play_board.board[row_index,colum_index : colum_index+ int(char):1] = 0
            print(char + " spaces added " + str(row_index) +" " + str(colum_index))
            colum_index += int(char)
            continue

        if char == "R":
            peice = copy.deepcopy(Rook(1)) 
        if char =="N":
            peice = copy.deepcopy(Knight(1))
        if char == "B":
            peice = copy.deepcopy(Bishop(1))
        if char =="Q":
            peice = copy.deepcopy(Queen(1))
        if char =="K":
            peice = copy.deepcopy(King(1))
        if char =="P":
            peice = copy.deepcopy(Pawn(1))
        if char == "r":
            peice = copy.deepcopy(Rook(-1)) 
        if char =="n":
            peice = copy.deepcopy(Knight(-1))
        if char == "b":
            peice = copy.deepcopy(Bishop(-1))
        if char =="q":
            peice = copy.deepcopy(Queen(-1))
        if char =="k":
            peice = copy.deepcopy(King(-1))
        if char =="p":
            peice = copy.deepcopy(Pawn(-1))

        play_board.add_peice(peice,row_index,colum_index)
        print( str(peice.__class__) + " added "+ str(row_index) + " " + str(colum_index))
        colum_index += 1
        #print(row_index)
    #print(play_board.board)
    return FEN

initalize_from_fen("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R")

print(play_board.get_bit_board())

QS.add_peice(2,2,"w_bishop.png")

# # pawn1 = Pawn(1)    
# # pawn2 = Pawn(1) 

# # pawn3 = Pawn(1) 
# # pawn4 = Pawn(1) 

# bishop1 = Bishop(1) 
# # knight1 = Knight(1) 

# rook1 = Rook(1)
# queen1 = Queen(1)
# king1 = King(1)

# # play_board.add_peice(pawn2,5,3)
# # play_board.add_peice(pawn1,6,2)
# # play_board.add_peice(pawn4,6,4)
# # play_board.add_peice(knight1,4,5)
# play_board.add_peice(bishop1,5,4)
# play_board.add_peice(rook1, 2,4)
# play_board.add_peice(queen1, 3,3)
# play_board.add_peice(king1,5,5)

# #print(play_board.bit_board)

# # print(pawn2.get_legal_moves())
# #print(play_board.bit_board)
# #print(rook1.get_legal_moves(play_board.bit_board))
# #print(queen1.get_legal_moves(play_board.bit_board))
# print(king1.get_legal_moves(play_board.bit_board))



# # print(pawn1.get_legal_moves())
# # print(pawn2.get_legal_moves())