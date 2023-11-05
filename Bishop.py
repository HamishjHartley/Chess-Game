import numpy as np
import Peice

#Bishop class which is a child class of Peice
class Bishop(Peice):
    def __init__(self, colour):
        Peice.__init__(self, colour) #to keep the inheritance of Peice's "__init__" function

    #Currently returns a list of all squares on left and right diagonals of bishop, ignoring other peices on diagonal
    def get_legal_moves(self):
        #TODO: Fix board reference, not directly to object instance. Means it will be coupled 
        board_state = play_board.get_bit_board() #Copies board state from bit board
        origin_pos = [self.v, self.h] #Peice's starting position at turn


        #up right
        search_pos = origin_pos #Peices current position, used as the start of the search
        while search_pos[0] <= 7 and search_pos[1] <= 7:
            if board_state[search_pos[0],search_pos[1]] == self.COLOUR: 
                break
            elif board_state[search_pos[0],search_pos[1]] == self.COLOUR *-1:
                self.legal_moves.append([search_pos[0], search_pos[1]])
                break
            self.legal_moves.append([search_pos[0], search_pos[1]])
            search_pos[0] += 1
            search_pos[1] += 1

        #down right
        search_pos = origin_pos #Peices current position, used as the start of the search
        while search_pos[0] >= 0 and search_pos[1] <= 7:
            if board_state[search_pos[0],search_pos[1]] == self.COLOUR: 
                break
            elif board_state[search_pos[0],search_pos[1]] == self.COLOUR *-1:
                self.legal_moves.append([search_pos[0], search_pos[1]])
                break
            self.legal_moves.append([search_pos[0], search_pos[1]])
            search_pos[0] -= 1
            search_pos[1] += 1

        #up left
        search_pos = origin_pos #Peices current position, used as the start of the search
        while search_pos[0] <= 7 and search_pos[1] >= 0:
            if board_state[search_pos[0],search_pos[1]] == self.COLOUR: 
                break
            elif board_state[search_pos[0],search_pos[1]] == self.COLOUR *-1:
                self.legal_moves.append([search_pos[0], search_pos[1]])
                break
            self.legal_moves.append([search_pos[0], search_pos[1]])
            search_pos[0] += 1
            search_pos[1] -= 1

        #down left
        search_pos = [self.v, self.h] #Peices current position, used as the start of the search
        while search_pos[0] >= 0 and search_pos[1] >= 0:
            if board_state[search_pos[0],search_pos[1]] == self.COLOUR: 
                break
            elif board_state[search_pos[0],search_pos[1]] == self.COLOUR *-1:
                self.legal_moves.append([search_pos[0], search_pos[1]])
                break
            self.legal_moves.append([search_pos[0], search_pos[1]])
            search_pos[0] -= 1
            search_pos[1] -= 1

        return self.legal_moves
