import sys
import os
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QPen, QColor, QPixmap

from Peice import Peice

#Function inspired from
# https://stackoverflow.com/questions/30230592/loading-all-images-using-imread-from-a-given-folder
#Loads an image dictionary which can be accessed through the icon filenames
def load_images_from_folder(folder):
    images = {}
    for filename in os.listdir(folder):
        img = QPixmap(os.path.join(folder,filename))
        if img is not None:
            images[filename] = img
    return images

#Extending the QLabel class so that peices can emmit signal when clicked
class ClickLabel(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self, event)

#Sets window dimensions
class Setting:
    WIDTH = 80
    HEIGHT = 80

#grid size
col, row = 8, 8

class QS(QGraphicsScene):
    def __init__(self, parent=None):
        super(QS, self).__init__(QtCore.QRectF(0, 0, col * Setting.WIDTH, row * Setting.HEIGHT), parent)

        self.peice_icons = load_images_from_folder("C:/Users/theha/Documents/Github/Chess-Game/icons")
        self.added_peices ={} #Dictionary to keep track of added peices to GUI

    #Creates a piece, with position [v,h] and type
    def create_peice(self,v: int, h:int ,peice_type: str):
        self.added_peices[v,h] = peice_type #keep track of added peices to GUI

        label = ClickLabel() #Creating an instance of the custom label class
        pixmap = self.peice_icons[peice_type]
        label.setPixmap(pixmap)
        label.move(10 + 80*h,10 + 80*v) #Set position of Piece on board (Label)
        label.clicked.connect(self.peice_click)
        return label

    def peice_click(self):
        print("Clicked")
        
    #Removes peice from Board
    def remove_peice(self,v: int, h:int):
        self.removeItem(self.added_peices[v,h]) 
        print("Removed peice")

    #TODO: Implement remove peice function which removes Pixmap from given [v,h]
    def move_peice(self,v: int, h: int, target_v:int, target_h:int):
        p = QtCore.QPointF(Setting.WIDTH*target_h, Setting.HEIGHT*target_v)
        self.added_peices[v,h].setPos(p) #Moves peice 
        self.added_peices[target_v,target_h] = self.added_peices[v,h] #Updates the location key for moved peice

    #TODO:Needs work
    def show_movement_squares(self, peice :Peice):
        moves = Peice.get_legal_moves() #Get list of legal moves
        for move in moves:
            self.highlight_square(move)
        pass

    #Renders a highlighted square at a set co-ordinate [v,h]
    def highlight_square(self,v:int,h:int):
        self.square = QtCore.QRectF(10+80*h,10+80*v,80,80)
        self.addRect(self.square,
                     pen=QtGui.QPen(),
                     brush=QtGui.QBrush())
        
    # def drawBackground(self, painter, rect):
    #     width = col * Setting.WIDTH
    #     height = row * Setting.HEIGHT

    #     l = QtCore.QLineF(QtCore.QPointF(0, 0), QtCore.QPointF(width, 0))
    #     for _ in range(row+1):
    #         painter.drawLine(l)
    #         l.translate(0, Setting.HEIGHT)

    #     l = QtCore.QLineF(QtCore.QPointF(0, 0), QtCore.QPointF(0, height))
    #     for _ in range(col+1):
    #         painter.drawLine(l)
    #         l.translate(Setting.WIDTH, 0)

class QV(QGraphicsView):
    pass

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.scene = QS(self)
        view = QV(self.scene)
        self.setCentralWidget(view)

    def add_peice(self,v:int,h:int, peice_type:str):
        peice_label = self.scene.create_peice(v,h, peice_type)   
        self.scene.addWidget(peice_label)

    def move_peice(self,v:int,h:int, target_v:int, target_h:int):
        self.scene.move_peice(v,h,target_v,target_h)

    def remove_peice(self,v: int, h:int):
        self.scene.remove_peice(v,h)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.add_peice(3,4,"w_bishop.png")

    w.show()
    sys.exit(app.exec_())