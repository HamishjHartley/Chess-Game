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

#GUI inports
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QPen, QColor, QPixmap
import sys
import os

from window2 import MainWindow


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
            #print("New line")
            continue # Go to next iteration and skip following code
        if char.isdigit() == True:
            play_board.board[row_index,colum_index : colum_index+ int(char):1] = 0
            #print(char + " spaces added " + str(row_index) +" " + str(colum_index))
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
        #print( str(peice.__class__) + " added "+ str(row_index) + " " + str(colum_index))
        colum_index += 1
        #print(row_index)
    #print(play_board.board)
    return FEN

initalize_from_fen("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R")


#https://stackoverflow.com/questions/419163/what-does-if-name-main-do Check this for an explanation
#if __name__ == "__main__":


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
