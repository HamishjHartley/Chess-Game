from Peice import Peice

class Queen(Peice):
    def __init__(self, colour:int):
        Peice.__init__(self, colour) #to keep the inheritance of Peice's "__init__" function
        #self.file_name = ["b_queen.png", "w_queen.png"]

    def get_file_name(self):
        if self.COLOUR == -1:
            return "b_queen.png"
        if self.COLOUR == 1:
            return "w_queen.png"

    def check_legal_move(self, v:int, h:int, bit_board):
        current_square = (v,h)
        if bit_board[current_square] == self.COLOUR:
            return -1
        if bit_board[current_square] == self.COLOUR*-1: #If opposite coloured piece on square
            self.legal_moves.append(current_square)
            return -1
        self.legal_moves.append(current_square)
        print("Added move " + str(v) + " " + str(h))

    def get_legal_moves(self, bit_board):
        board_state = bit_board
        origin_pos = [self.v, self.h]

        #up
        search_pos = [self.v, self.h]
        search_pos[0] += 1
        while search_pos[0] <=7:
            if self.check_legal_move(search_pos[0],search_pos[1],bit_board) == -1:
                break
            search_pos[0] += 1

        #down
        search_pos = [self.v, self.h]
        search_pos[0] -= 1
        while search_pos[0] >=0:
            if self.check_legal_move(search_pos[0],search_pos[1],bit_board) == -1:
                break
            search_pos[0] -= 1

        #left
        search_pos = [self.v, self.h]
        search_pos[1] -= 1
        while search_pos[1] >=0:
            if self.check_legal_move(search_pos[0],search_pos[1],bit_board) == -1:
                break
            search_pos[1] -= 1

        #right
        search_pos = [self.v, self.h]
        search_pos[1] += 1
        while search_pos[1] <=7:
            if self.check_legal_move(search_pos[0],search_pos[1],bit_board) == -1:
                break
            search_pos[1] += 1

               #up right
        search_pos = [self.v, self.h]
        search_pos[0] += 1
        search_pos[1] += 1
        while search_pos[0] <= 7 and search_pos[1] <= 7:
            if self.check_legal_move(search_pos[0],search_pos[1],bit_board) == -1:
                break
            search_pos[0] += 1
            search_pos[1] += 1

        #down right
        search_pos = [self.v, self.h] #Peices current position, used as the start of the search
        search_pos[0] -= 1
        search_pos[1] += 1
        while search_pos[0] >= 0 and search_pos[1] <= 7:
            if self.check_legal_move(search_pos[0],search_pos[1],bit_board) == -1:
                break
            search_pos[0] -= 1
            search_pos[1] += 1

        #up left
        search_pos = [self.v, self.h] #Peices current position, used as the start of the search
        search_pos[0] += 1
        search_pos[1] -= 1
        while search_pos[0] <= 7 and search_pos[1] >= 0:
            if self.check_legal_move(search_pos[0],search_pos[1],bit_board) == -1:
                break
            search_pos[0] += 1
            search_pos[1] -= 1

        #down left
        search_pos = [self.v, self.h] #Peices current position, used as the start of the search
        search_pos[0] -= 1
        search_pos[1] -= 1
        while search_pos[0] >= 0 and search_pos[1] >= 0:
            if self.check_legal_move(search_pos[0],search_pos[1],bit_board) == -1:
                break
            search_pos[0] -= 1
            search_pos[1] -= 1


        print(bit_board)
        return self.legal_moves