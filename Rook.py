from Peice import Peice

class Rook(Peice):
    def __init__(self, colour):
        Peice.__init__(self, colour) #to keep the inheritance of Peice's "__init__" function
    
    def get_legal_moves(self, bit_board):
        board_state = bit_board
        origin_pos = [self.v, self.h]

        #up
        search_pos = [self.v, self.h]
        while search_pos[0] <=7:
            self.legal_moves.append([search_pos[0], search_pos[1]])
            #print("Added move " + str(search_pos[0]) + " " + str(search_pos[1]))
            #bit_board[search_pos] = 9
            search_pos[0] += 1

        #down
        search_pos = [self.v, self.h]
        while search_pos[0] >=0:
            self.legal_moves.append([search_pos[0], search_pos[1]])
            #print("Added move " + str(search_pos[0]) + " " + str(search_pos[1]))
            #bit_board[search_pos] = 9
            search_pos[0] -= 1

        #left
        search_pos = [self.v, self.h]
        while search_pos[1] >=0:
            self.legal_moves.append([search_pos[0], search_pos[1]])
            #print("Added move " + str(search_pos[0]) + " " + str(search_pos[1]))
            #bit_board[search_pos] = 9
            search_pos[1] -= 1

        #right
        search_pos = [self.v, self.h]
        while search_pos[1] <=7:
            self.legal_moves.append([search_pos[0], search_pos[1]])
            #bit_board[search_pos] = 9
            search_pos[1] += 1

        #print(bit_board)
        return self.legal_moves
