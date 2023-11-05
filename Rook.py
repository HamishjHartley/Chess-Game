from Peice import Peice

class Rook(Peice):
    def __init__(self, colour):
        Peice.__init__(self, colour) #to keep the inheritance of Peice's "__init__" function
    
    def get_legal_moves(self, bit_board):
        board_state = bit_board
        origin_pos = [self.v, self.h]

        #up
        search_pos = origin_pos
        while search_pos[0] <=7:
            if board_state[search_pos[0],search_pos[1]] == self.COLOUR: 
                break
            elif board_state[search_pos[0],search_pos[1]] == self.COLOUR *-1:
                self.legal_moves.append([search_pos[0], search_pos[1]])
                break
            self.legal_moves.append([search_pos[0], search_pos[1]])
            search_pos[0] += 1

        #down
        search_pos = origin_pos
        while search_pos[0] >=0:
            if board_state[search_pos[0],search_pos[1]] == self.COLOUR: 
                break
            elif board_state[search_pos[0],search_pos[1]] == self.COLOUR *-1:
                self.legal_moves.append([search_pos[0], search_pos[1]])
                break
            self.legal_moves.append([search_pos[0], search_pos[1]])
            search_pos[0] -= 1

        #left
        search_pos = origin_pos
        while search_pos[1] >=0:
            if board_state[search_pos[0],search_pos[1]] == self.COLOUR: 
                break
            elif board_state[search_pos[0],search_pos[1]] == self.COLOUR *-1:
                self.legal_moves.append([search_pos[0], search_pos[1]])
                break
            self.legal_moves.append([search_pos[0], search_pos[1]])
            search_pos[1] -= 1

        #right
        search_pos = origin_pos
        while search_pos[1] <=7:
            if board_state[search_pos[0],search_pos[1]] == self.COLOUR: 
                break
            elif board_state[search_pos[0],search_pos[1]] == self.COLOUR *-1:
                self.legal_moves.append([search_pos[0], search_pos[1]])
                break
            self.legal_moves.append([search_pos[0], search_pos[1]])
            search_pos[1] += 1

        return self.legal_moves
