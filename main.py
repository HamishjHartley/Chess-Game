# git add main.py
# git commit -m "TEST"
# git push origin main

import numpy as np

#TODO: possibly create Move class, or move this to Board class
move_stack =[]

#Peice Parent class, from which all peice types inherit
class Peice:
    #Constructor which initiialzes the vertial and horizontal position of the Peice
    #TODO: throw exception if colour not 0 or 1
    def __init__(self, colour):
        self.COLOUR = colour #Colour class constant, 1 = W, -1 = B
        self.v = 0
        self.h = 0
        self.legal_moves =[]
        self.is_captured = False
        
    #Updates the associated vertical and horizontal postion so the peice can keep track of it's location
    def update_position(self, v, h):
        self.v = v
        self.h = h

    #Returns the current location of the peice
    def current_position(self):
        return self.v, self.h
    
#Pawn class which is a child class of Peice
class Pawn(Peice):
    def __init__(self, colour):
        Peice.__init__(self, colour) #to keep the inheritance of Peice's "__init__" function

    #Returns a list of legal move(s) specific to a Pawn peice
    def get_legal_moves(self):
        #Pawns movement rules
        self.straight_ahead = (self.v+1, self.h)
        self.capture_left = (self.v+1, self.h-1)
        self.capture_right = (self.v+1, self.h+1)

        #Search through adjecent squares in board array, 
        if play_board.board[self.straight_ahead] == 0:
            self.legal_moves.append(self.straight_ahead)
        #elif board[LEFT] == opposite coloured Peice


        #elif play_board.board[self.capture_left]:
        #   self.legal_moves.append(square index)
        #elif (capture square RIGHT) has enemyPeice:
        #   self.legal_moves.append(square index)
        return self.legal_moves
    
    class Bishop(Peice):
        def __init__(self, colour):
            Peice.__init__(self, colour) #to keep the inheritance of Peice's "__init__" function

        def get_legal_moves(self):
            #TODO: Fix board reference, not directly to object instance. Means it will be coupled 
            board_state = play_board.bit_board #Copies board state from bit board

            search_pos = (self.v, self.h) #Peices current position, used as the start of the search
            

            #up right
            while(board_state[search_pos] != None or board_state != self.COLOUR): #TODO: FIX: Currently adds peice's initial position to legal_moves 
                self.legal_moves.append(search_pos)
                search_pos[0] += 1
                search_pos[1] += 1
            

            #down right
            #up left
            #down right
            return self.legal_moves


#Board class
#is the controller class to which "Peices" are added, handles events/interaction's between peices
class Board:
    #constructor to initialize 8x8 board array
    def __init__(self):
        self.board = np.zeros((8,8), dtype=Peice)

        #"bit board" to hold the state of each square on the board for easier move/capture calculation
        self.bit_board = np.zeros((8,8), dtype=int)


    #Adds a peice to a position on the 8x8 board array defined by index (pos)
    #TODO: Throw exception if position reference out of bounds of board array
    def add_peice(self, Peice, v, h):
        self.board[v,h]= Peice
        Peice.update_position(v, h)

        #Simulatniously update bit board with the associated integer value for each sqaure. 
        self.bit_board[v, h] = Peice.COLOUR

    #Removes a given peice from the 8x8 board array(By replacing with a 0)
    #TODO:Find a better way to do this
    def remove_peice(self, Peice):
        #np.delete(self.board, [Peice.currentPosition()])
        self.board[Peice.current_position()]= 0
    
    # #Moves a given peice to a target position
    #by removing from origional square and adding it to target square
    #TODO:Find better way to do this
    def move_peice(self, Peice, v, h):
        self.remove_peice(Peice)
        self.add_peice(Peice, v, h)

play_board = Board() 

pawn1 = Pawn(1) #White pawn    
pawn2 = Pawn(-1) #Black pawn

play_board.add_peice(pawn1,1,4) #Add e2 pawn to board (WHITE)
play_board.add_peice(pawn2,6,3) #Add d7 pawn to board (BLACK)

print(play_board.bit_board)

play_board.move_peice(pawn1,7,7)
print(play_board.bit_board)

# print(pawn1.get_legal_moves())
# print(pawn2.get_legal_moves())