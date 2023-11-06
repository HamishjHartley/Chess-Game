import sys
import os
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QPen, QColor, QPixmap

#Function inspired from
# https://stackoverflow.com/questions/30230592/loading-all-images-using-imread-from-a-given-folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = QPixmap(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

#Sets window dimensions, grid size
class Setting:
    WIDTH = 80
    HEIGHT = 80

X, Y = 8, 8


class QS(QGraphicsScene):
    def __init__(self, parent=None):
        super(QS, self).__init__(QtCore.QRectF(0, 0, X * Setting.WIDTH, Y * Setting.HEIGHT), parent)

        peice_icons = load_images_from_folder("C:/Users/theha/OneDrive/Desktop/Chess-Game/gui/icons")

        p = QtCore.QPointF()
        for i in range(X):
            p = QtCore.QPointF(Setting.WIDTH*i, 0)
            for j in range(Y):
                it = self.addPixmap(peice_icons[i])
                it.setPos(p)
                p += QtCore.QPointF(0, Setting.HEIGHT)

    def drawBackground(self, painter, rect):
        width = X * Setting.WIDTH
        height = Y * Setting.HEIGHT

        l = QtCore.QLineF(QtCore.QPointF(0, 0), QtCore.QPointF(width, 0))
        for _ in range(Y+1):
            painter.drawLine(l)
            l.translate(0, Setting.HEIGHT)

        l = QtCore.QLineF(QtCore.QPointF(0, 0), QtCore.QPointF(0, height))
        for _ in range(X+1):
            painter.drawLine(l)
            l.translate(Setting.WIDTH, 0)


class QV(QGraphicsView):
    pass


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        scene = QS(self)
        view = QV(scene)
        self.setCentralWidget(view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())