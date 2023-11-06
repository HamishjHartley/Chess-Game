import sys
import os
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QPen, QColor, QPixmap


#Function inspired from
# https://stackoverflow.com/questions/30230592/loading-all-images-using-imread-from-a-given-folder
#Loads an image dictionary which can be accessed through the icon filenames
def load_images_from_folder(folder):
    images = {}
    for filename in os.listdir(folder):
        img = QPixmap(os.path.join(folder,filename))
        if img is not None:
            images[filename] = img
    print(images)
    return images

#Sets window dimensions
class Setting:
    WIDTH = 80
    HEIGHT = 80

#grid size
col, row = 8, 8

class QS(QGraphicsScene):
    def __init__(self, parent=None):
        super(QS, self).__init__(QtCore.QRectF(0, 0, col * Setting.WIDTH, row * Setting.HEIGHT), parent)

        self.peice_icons = load_images_from_folder("C:/Users/theha/OneDrive/Desktop/Chess-Game/icons")


    def add_peice(self,v ,h ,peice_type):
        p = QtCore.QPointF()
        p = QtCore.QPointF(Setting.WIDTH*h, Setting.HEIGHT*v)
        it = self.addPixmap(self.peice_icons[peice_type])
        it.setPos(p)
        #p += QtCore.QPointF(0, Setting.HEIGHT)


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
        scene = QS(self)
        scene.add_peice(2,3,"w_bishop.png")
        scene.add_peice(5,4,"b_knight.png")
        
        #scene.add_peice()
        view = QV(scene)
        self.setCentralWidget(view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())