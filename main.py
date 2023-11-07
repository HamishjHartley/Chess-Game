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

app = QApplication(sys.argv)
w = MainWindow()

#Initializes game based on FEN code
def initalize_from_fen(FEN:str):
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
            w.add_peice(row_index,colum_index,"w_rook.png") 
        if char =="N":
            peice = copy.deepcopy(Knight(1))
            w.add_peice(row_index,colum_index,"w_knight.png")
        if char == "B":
            peice = copy.deepcopy(Bishop(1))
            w.add_peice(row_index,colum_index,"w_bishop.png")
        if char =="Q":
            peice = copy.deepcopy(Queen(1))
            w.add_peice(row_index,colum_index,"w_queen.png")
        if char =="K":
            peice = copy.deepcopy(King(1))
            w.add_peice(row_index,colum_index,"w_king.png")
        if char =="P":
            peice = copy.deepcopy(Pawn(1))
            w.add_peice(row_index,colum_index,"w_pawn.png")
        if char == "r":
            peice = copy.deepcopy(Rook(-1)) 
            w.add_peice(row_index,colum_index,"b_rook.png")
        if char =="n":
            peice = copy.deepcopy(Knight(-1))
            w.add_peice(row_index,colum_index,"b_knight.png")
        if char == "b":
            peice = copy.deepcopy(Bishop(-1))
            w.add_peice(row_index,colum_index,"b_bishop.png")
        if char =="q":
            peice = copy.deepcopy(Queen(-1))
            w.add_peice(row_index,colum_index,"b_queen.png")
        if char =="k":
            peice = copy.deepcopy(King(-1))
            w.add_peice(row_index,colum_index,"b_king.png")
        if char =="p":
            peice = copy.deepcopy(Pawn(-1))
            w.add_peice(row_index,colum_index,"b_pawn.png")

        play_board.add_peice(peice,row_index,colum_index)
        colum_index += 1
    return FEN

pawn1 = Pawn(1)
play_board.add_peice(pawn1,2,3)
w.add_peice(2,3,"w_pawn.png")

#Move a given peice to a target position [v,h], links GUI with backend 
#TODO: change FEN implementation so each peice object has a unique identfier
def move_peice(Peice : Peice, v: int,h :int):
    w.move_peice(Peice.v, Peice.h, v,h) #Moves peice in GUI
    play_board.move_peice(Peice,v,h) #Moves peice in Backend

#initalize_from_fen("rnbqkb1r/ppp2ppp/4pn2/3p4/3P1B2/4PN2/PPP2PPP/RN1QKB1R")

move_peice(pawn1,4,4)
#w.remove_peice(5,5)

w.show()
sys.exit(app.exec_())