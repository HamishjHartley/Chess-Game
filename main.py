# git add main.py
# git commit -m "TEST"
# git push origin master

import numpy as np

#TODO: possibly create Move class, or move this to Board class
move_stack =[]

#Peice Parent class, from which all peice types inherit
class Peice:
    #Constructor which initiialzes the vertial and horizontal position of the Peice
    def __init__(self):
        self.pos_vert = 0
        self.pos_hor = 0
        self.legal_moves =[]
        
    #Updates the associated vertical and horizontal postion so the peice can keep track of it's location
    def updatePosition(self, pos_vert, pos_hor):
        self.pos_vert = pos_vert
        self.pos_hor = pos_hor

    #Returns the current location of the peice
    def currentPosition(self):
        return self.pos_vert, self.pos_hor
    
#Pawn class which is a child class of Peice
class Pawn(Peice):
    def __init__(self):
        Peice.__init__(self) #to keep the inheritance of Peice's "__init__" function

    #Returns a list of legal move(s) specific to a Pawn peice
    def getLegalMoves(self, Board):
        #Search through adjecent squares in board array, 
        #by adding [vertical +1 , horiztonal +0 ] (Straight ahead)
        Board.board[]
        #[vertial + 1, horizontal -1], [vertical +1, horizontal +1] (capture squares)

        #if (straight ahead) sqaure is empty:
        #   self.legal_moves.append(square index)
        #elif (capture square LEFT) has enemyPeice:
        #   self.legal_moves.append(square index)
        #elif (capture square RIGHT) has enemyPeice:
        #   self.legal_moves.append(square index)

        return self.legal_moves


#Board class
#is the controller class to which "Peices" are added, 
class Board:
    #constructor to initialize 8x8 board array
    def __init__(self):
        self.board = np.zeros((8,8), dtype=Peice)

    #Adds a peice to a position on the 8x8 board array defined by index (pos)
    def addPeice(self, Peice, pos_vert, pos_hor):
        self.board[pos_vert,pos_hor]= Peice
        Peice.updatePosition(pos_vert, pos_hor)

    #Removes a given peice from the 8x8 board array(By replacing with a 0)
    #TODO:Find a better way to do this
    def removePeice(self, Peice):
        #np.delete(self.board, [Peice.currentPosition()])
        self.board[Peice.currentPosition()]= 0
    
    # #Moves a given peice to a target position
    #by removing from origional square and adding it to target square
    #TODO:Find better way to do this
    def movePeice(self, Peice, pos_vert, pos_hor):
        self.board.removePeice(Peice)
        self.board.addPeice(Peice, pos_vert, pos_hor)
        

play_board = Board() 

p1 = Peice()    


#print(p1.currentPosition()[0])

play_board.addPeice(p1,4,2)
print(p1.currentPosition()[0])

print(play_board.board)
play_board.removePeice(p1)

print(play_board.board)