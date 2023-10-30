# git add main.py
# git commit -m "TEST"
# git push origin master

import numpy as np

move_stack =[]

#Peice class
class Peice:
    #Constructor which initiialzes the x and y position of the Peice
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        
    #Updates the associated x and y postion so the peice can keep track of it's location
    def updatePosition(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    #Returns the current location of the peice
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

    #Removes a given peice from the 8x8 board array(By replacing with a 0)
    #Find a better way to do this
    def removePeice(self, Peice):
        #np.delete(self.board, [Peice.currentPosition()])
        self.board[Peice.currentPosition()]= 0
    
    # #Moves a given peice to a target position
    #by removing from origional square and adding it to target square
    def movePeice(self, Peice, pos_x, pos_y):
        self.board.removePeice(Peice)
        self.board.addPeice(Peice, pos_x, pos_y)
        

play_board = Board() 

p1 = Peice()    


#print(p1.currentPosition()[0])

play_board.addPeice(p1,4,2)
print(p1.currentPosition()[0])

print(play_board.board)
play_board.removePeice(p1)

print(play_board.board)