import sys
import os
import typing
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QMouseEvent, QPainter, QPen, QColor, QPixmap

from Board import Board
from Peice import Peice
from Rook import Rook
from Bishop import Bishop
from Queen import Queen
from Pawn import Pawn
#Sets window dimensions
class Setting:
    WIDTH = 80
    HEIGHT = 80

#grid size
col, row = 8, 8

play_board = Board()

rook1 = Rook(1)
bishop1 = Bishop(1)
bishop0 = Bishop(-1)
queen0 = Queen(-1)
pawn1 = Pawn(-1)
pawn0 = Pawn(1)

play_board.add_peice(rook1, 3,5)
# play_board.add_peice(bishop1,2,5)
# play_board.add_peice(bishop0,1,4)
# play_board.add_peice(queen0,3,4)
# play_board.add_peice(pawn1,2,2)
# play_board.add_peice(pawn0,1,3)


#Loads an image dictionary which can be accessed through the icon filenames
def load_images_from_folder(folder):
    images = {}
    for filename in os.listdir(folder):
        img = QPixmap(os.path.join(folder,filename))
        if img is not None:
            images[filename] = img
    return images

#Custom ClickLabel which extends behaviour of QLabel, overriding mousePressEvent()
class ClickLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self, event)

class ClickRect(QtCore.QRectF):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self, event)


class QS(QGraphicsScene):
    def __init__(self, parent=None):
        super(QS, self).__init__(QtCore.QRectF(0, 0, col * Setting.WIDTH, row * Setting.HEIGHT), parent)

        self.peice_icons = load_images_from_folder("C:/Users/theha/Documents/GitHub/Chess-Game/icons")

        self.added_peices ={} #Dictionary to keep track of added peices to GUI
        self.rendered_moves= []

    def add_peice(self,v: int, h:int ,peice: Peice):
        peice_label = ClickLabel() 
        pixmap = self.peice_icons[peice.get_file_name()] #creates a pixmap from the peice_icon's dictionary
        peice_label.setPixmap(pixmap)
        peice_label.move(10+80*h,10+80*v) #Set position of peice_label given by [v,h]
        self.addWidget(peice_label)
        self.added_peices[v,h] = peice_label

        peice_label.clicked.connect(lambda: self.show_moves(peice))
        
    def remove_peice(self,v: int, h:int):
        self.added_peices[v,h] = None
        #self.removeWidget(self.added_peices[v,h]) 
        #print("Removed peice")

    #TODO: Implement remove peice function which removes Pixmap from given [v,h]
    def move_peice(self,v: int, h: int, target_v:int, target_h:int):
       self.added_peices[v,h].move(10+80*target_h,10+80*target_v)
       self.added_peices[target_v,target_h] = self.added_peices[v,h] #Updates the location key for moved peice

    #Highlights a square on board defined by [v,h]
    def highlight_square(self,v:int,h:int, peice:Peice):
        square_label = ClickLabel()
        pixmap = self.peice_icons["select.png"] #creates a pixmap from the peice_icon's dictionary
        square_label.move(10+80*h,10+80*v) #Set position of peice_label given by [v,h]
        square_label.setGeometry(10+80*h,10+80*v,40,40)
        self.addWidget(square_label)
        square_label.clicked.connect(lambda : self.move_peice(peice.v,peice.h,v,h))
        return square_label
    
        square = ClickRect(80*h,80*v,80,80)
        square.clicked.connect(lambda: self.move_peice(peice.v,peice.h,v,h))
        return self.addRect(square,
                     QPen(QtCore.Qt.red,  1, QtCore.Qt.SolidLine),
                      QBrush(QtCore.Qt.red, QtCore.Qt.FDiagPattern)
         )

    def show_moves(self,peice: Peice):
        #Loops through currently rendered moves and removes them from screen
        for rendered_move in self.rendered_moves:
            rendered_move.clear()
        self.rendered_moves.clear() #Clears list of rendered moves

        state_board = play_board.bit_board
        moves = peice.get_legal_moves(state_board)
        #For each legal move, render corresponding square on board
        for move in moves:
            self.rendered_moves.append(self.highlight_square(move[0], move[1],peice))
        #print(state_board)
        print(play_board.board)


    def drawBackground(self, painter, rect):
        width = col * Setting.WIDTH
        height = row * Setting.HEIGHT

        l = QtCore.QLineF(QtCore.QPointF(0, 0), QtCore.QPointF(width, 0))
        for _ in range(row+1):
            painter.drawLine(l)
            l.translate(0, Setting.HEIGHT)

        l = QtCore.QLineF(QtCore.QPointF(0, 0), QtCore.QPointF(0, height))
        for _ in range(col+1):
            painter.drawLine(l)
            l.translate(Setting.WIDTH, 0)

class QV(QGraphicsView):
    pass

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.scene = QS(self)
        view = QV(self.scene)
        self.setCentralWidget(view)

    def add_peice(self,v:int,h:int, peice_type:str):
        self.scene.add_peice(v,h, peice_type)   

        #self.added_peices.append([v,h,peice_type])

    def move_peice(self,v:int,h:int, target_v:int, target_h:int):
        self.scene.move_peice(v,h,target_v,target_h)
        play_board.move_peice(rook1,target_v,target_h)

    def remove_peice(self,v: int, h:int):
        self.scene.remove_peice(v,h)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()

    w.add_peice(3,5,rook1)
    # w.add_peice(2,5,bishop1)
    # w.add_peice(1,4,bishop0)
    # w.add_peice(3,4,queen0)
    # w.add_peice(2,2,pawn1)
    # w.add_peice(1,3,pawn0)

    # w.move_peice(2,2,5,5)
    # play_board.move_peice(pawn1,5,5)

    w.show()
    sys.exit(app.exec_())
