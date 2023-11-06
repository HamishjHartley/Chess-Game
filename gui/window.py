import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush, QPen, QColor, QPixmap
from PyQt5.QtCore import Qt



app = QApplication(sys.argv)

# Defining a scene rect of 400x200, with it's origin at 0,0.
# If we don't set this on creation, we can set it later with .setSceneRect
scene = QGraphicsScene(0, 0, 500, 500)

image = QPixmap("Chess_rlt60.png")




# Draw a rectangle item, setting the dimensions.
#row 1
a1 = QGraphicsRectItem(0,0,50,50)
b1 = QGraphicsRectItem(50,0,50,50)
c1 = QGraphicsRectItem(100,0,50,50)
d1 = QGraphicsRectItem(150,0,50,50)
e1 = QGraphicsRectItem(200,0,50,50)
f1 = QGraphicsRectItem(250,0,50,50)
g1 = QGraphicsRectItem(300,0,50,50)
h1 = QGraphicsRectItem(350,0,50,50)



#row2
b2 = QGraphicsRectItem(50,50,50,50)
a2 = QGraphicsRectItem(0,50,50,50)
c2 = QGraphicsRectItem(100,50,50,50)
d2 = QGraphicsRectItem(150,50,50,50)
e2 = QGraphicsRectItem(200,50,50,50)
f2 = QGraphicsRectItem(250,50,50,50)
g2 = QGraphicsRectItem(300,50,50,50)
h2 = QGraphicsRectItem(350,50,50,50)

#row 3
a3 = QGraphicsRectItem(0,100,50,50)
b3 = QGraphicsRectItem(50,100,50,50)
c3 = QGraphicsRectItem(100,100,50,50)
d3 = QGraphicsRectItem(150,100,50,50)
e3 = QGraphicsRectItem(200,100,50,50)
f3 = QGraphicsRectItem(250,100,50,50)
g3 = QGraphicsRectItem(300,100,50,50)
h3 = QGraphicsRectItem(350,100,50,50)

#row 4
a4 = QGraphicsRectItem(0,150,50,50)
b4 = QGraphicsRectItem(50,150,50,50)
c4 = QGraphicsRectItem(100,150,50,50)
d4 = QGraphicsRectItem(150,150,50,50)
e4 = QGraphicsRectItem(200,150,50,50)
f4 = QGraphicsRectItem(250,150,50,50)
g4 = QGraphicsRectItem(300,150,50,50)
h4 = QGraphicsRectItem(350,150,50,50)

#row 5
b5 = QGraphicsRectItem(50,200,50,50)
a5 = QGraphicsRectItem(0,200,50,50)
c5 = QGraphicsRectItem(100,200,50,50)
d5 = QGraphicsRectItem(150,200,50,50)
e5 = QGraphicsRectItem(200,200,50,50)
f5 = QGraphicsRectItem(250,200,50,50)
g5 = QGraphicsRectItem(300,200,50,50)
h5 = QGraphicsRectItem(350,200,50,50)

#row 6
a6 = QGraphicsRectItem(0,250,50,50)
b6 = QGraphicsRectItem(50,250,50,50)
c6 = QGraphicsRectItem(100,250,50,50)
d6 = QGraphicsRectItem(150,250,50,50)
e6 = QGraphicsRectItem(200,250,50,50)
f6 = QGraphicsRectItem(250,250,50,50)
g6 = QGraphicsRectItem(300,250,50,50)
h6 = QGraphicsRectItem(350,250,50,50)

#row 7
b7 = QGraphicsRectItem(50,300,50,50)
a7 = QGraphicsRectItem(0,300,50,50)
c7 = QGraphicsRectItem(100,300,50,50)
d7 = QGraphicsRectItem(150,300,50,50)
e7 = QGraphicsRectItem(200,300,50,50)
f7 = QGraphicsRectItem(250,300,50,50)
g7 = QGraphicsRectItem(300,300,50,50)
h7 = QGraphicsRectItem(350,300,50,50)

#row 8
a8 = QGraphicsRectItem(0,350,50,50)
b8 = QGraphicsRectItem(50,350,50,50)
c8 = QGraphicsRectItem(100,350,50,50)
d8 = QGraphicsRectItem(150,350,50,50)
e8 = QGraphicsRectItem(200,350,50,50)
f8 = QGraphicsRectItem(250,350,50,50)
g8 = QGraphicsRectItem(300,350,50,50)
h8 = QGraphicsRectItem(350,350,50,50)



# # Set the origin (position) of the rectangle in the scene.
# #row 1
# a1.setPos(0,0)
# b1.setPos(0,0)
# c1.setPos(0,0)
# d1.setPos(0,0)
# e1.setPos(0,0)
# f1.setPos(0,0)
# g1.setPos(0,0)
# h1.setPos(0,0)

# #row 2
# a2.setPos(0,0)
# b2.setPos(0,0)
# c2.setPos(0,0)
# d2.setPos(0,0)
# e2.setPos(0,0)
# f2.setPos(0,0)
# g2.setPos(0,0)
# h2.setPos(0,0)

# #row 3
# a3.setPos(0,0)
# b3.setPos(0,0)
# c3.setPos(0,0)
# d3.setPos(0,0)
# e3.setPos(0,0)
# f3.setPos(0,0)
# g3.setPos(0,0)
# h3.setPos(0,0)

# #row 4
# a4.setPos(0,0)
# b4.setPos(0,0)
# c4.setPos(0,0)
# d4.setPos(0,0)
# e4.setPos(0,0)
# f4.setPos(0,0)
# g4.setPos(0,0)
# h4.setPos(0,0)

# #row 5
# a5.setPos(0,0)
# b5.setPos(0,0)
# c5.setPos(0,0)
# d5.setPos(0,0)
# e5.setPos(0,0)
# f5.setPos(0,0)
# g5.setPos(0,0)
# h5.setPos(0,0)

# #row 6
# a6.setPos(0,0)
# b6.setPos(0,0)
# c6.setPos(0,0)
# d6.setPos(0,0)
# e6.setPos(0,0)
# f6.setPos(0,0)
# g6.setPos(0,0)
# h6.setPos(0,0)

# #row 7
# a7.setPos(0,0)
# b7.setPos(0,0)
# c7.setPos(0,0)
# d7.setPos(0,0)
# e7.setPos(0,0)
# f7.setPos(0,0)
# g7.setPos(0,0)
# h7.setPos(0,0)

# #row 8
# a8.setPos(0,0)
# b8.setPos(0,0)
# c8.setPos(0,0)
# d8.setPos(0,0)
# e8.setPos(0,0)
# f8.setPos(0,0)
# g8.setPos(0,0)
# h8.setPos(0,0)

# Define the brush (fill).


cream= QColor(183, 169, 128, 255)

highlight =QColor(202, 109, 109, 255)
black = QBrush(Qt.black) #black squares
white = QBrush(cream) #white squares



#row 1
a1.setBrush(black)
b1.setBrush(white)
c1.setBrush(black)
d1.setBrush(white)
e1.setBrush(black)
f1.setBrush(white)
g1.setBrush(black)
h1.setBrush(white)

#row 2
a2.setBrush(white)
b2.setBrush(black)
c2.setBrush(white)
d2.setBrush(black)
e2.setBrush(white)
f2.setBrush(black)
g2.setBrush(white)
h2.setBrush(black)

#row 3
a3.setBrush(black)
b3.setBrush(white)
c3.setBrush(black)
d3.setBrush(white)
e3.setBrush(black)
f3.setBrush(white)
g3.setBrush(black)
h3.setBrush(white)

#row 4
a4.setBrush(white)
b4.setBrush(black)
c4.setBrush(white)
d4.setBrush(black)
e4.setBrush(white)
f4.setBrush(black)
g4.setBrush(white)
h4.setBrush(black)

#row 5
a5.setBrush(black)
b5.setBrush(white)
c5.setBrush(black)
d5.setBrush(white)
e5.setBrush(black)
f5.setBrush(white)
g5.setBrush(black)
h5.setBrush(white)

#row 6
a6.setBrush(white)
b6.setBrush(black)
c6.setBrush(white)
d6.setBrush(black)
e6.setBrush(white)
f6.setBrush(black)
g6.setBrush(white)
h6.setBrush(black)

#row 7
a7.setBrush(black)
b7.setBrush(white)
c7.setBrush(black)
d7.setBrush(white)
e7.setBrush(black)
f7.setBrush(white)
g7.setBrush(black)
h7.setBrush(white)

#row 8
a8.setBrush(white)
b8.setBrush(black)
c8.setBrush(white)
d8.setBrush(black)
e8.setBrush(white)
f8.setBrush(black)
g8.setBrush(white)
h8.setBrush(black)

# Define the pen (line)
# pen = QPen(Qt.cyan)
# pen.setWidth(10)
# a1.setPen(pen)

#row1
scene.addItem(a1)
scene.addItem(b1)
scene.addItem(c1)
scene.addItem(d1)
scene.addItem(e1)
scene.addItem(f1)
scene.addItem(g1)
scene.addItem(h1)
#row 2
scene.addItem(a2)
scene.addItem(b2)
scene.addItem(c2)
scene.addItem(d2)
scene.addItem(e2)
scene.addItem(f2)
scene.addItem(g2)
scene.addItem(h2)
#row 3
scene.addItem(a3)
scene.addItem(b3)
scene.addItem(c3)
scene.addItem(d3)
scene.addItem(e3)
scene.addItem(f3)
scene.addItem(g3)
scene.addItem(h3)
#row 4
scene.addItem(a4)
scene.addItem(b4)
scene.addItem(c4)
scene.addItem(d4)
scene.addItem(e4)
scene.addItem(f4)
scene.addItem(g4)
scene.addItem(h4)
#row 5
scene.addItem(a5)
scene.addItem(b5)
scene.addItem(c5)
scene.addItem(d5)
scene.addItem(e5)
scene.addItem(f5)
scene.addItem(g5)
scene.addItem(h5)
#row 6
scene.addItem(a6)
scene.addItem(b6)
scene.addItem(c6)
scene.addItem(d6)
scene.addItem(e6)
scene.addItem(f6)
scene.addItem(g6)
scene.addItem(h6)
#row 7
scene.addItem(a7)
scene.addItem(b7)
scene.addItem(c7)
scene.addItem(d7)
scene.addItem(e7)
scene.addItem(f7)
scene.addItem(g7)
scene.addItem(h7)
#row 8
scene.addItem(a8)
scene.addItem(b8)
scene.addItem(c8)
scene.addItem(d8)
scene.addItem(e8)
scene.addItem(f8)
scene.addItem(g8)
scene.addItem(h8)

view = QGraphicsView(scene)
view.show()
app.exec_()