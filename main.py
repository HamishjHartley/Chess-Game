import numpy as np

#board = np.zeros([8,8]) #Chess board as an 8x8 array

move_stack =[]

#Peice class
class Peice:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        
    def updatePosition(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def currentPosition(self):
        return self.pos_x, self.pos_y
    
#board class
class Board:
    #constructor to initialize 8x8 board array
    def __init__(self):
        self.board = np.zeros((8,8), dtype=Peice)

    #Adds a peice to a position on the 8x8 board array defined by index (pos)
    def addPeice(self, Peice, pos_x, pos_y):
        self.board[pos_x,pos_y]= Peice
        Peice.updatePosition(pos_x, pos_y)

    #Removes a given peice from the 8x8 board array 
    # def removePeice(Peice, self):
        
    
    # #Moves a given peice to a target position
    # def movePeice(Peice, target, self):
    #     self.board

play_board = Board() 

p1 = Peice()    
p2 = Peice()
p3 = Peice()

play_board.addPeice(p1,4,2)
play_board.addPeice(p2, 5,7)
play_board.addPeice(p3,7,7)


print(p1.currentPosition())
print(p2.currentPosition())
print(p3.currentPosition())