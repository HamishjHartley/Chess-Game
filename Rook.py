import Peice

class Rook(Peice):
    def __init__(self, colour):
        Peice.__init__(self, colour) #to keep the inheritance of Peice's "__init__" function
    
    def get_legal_moves(self):
        return self.legal_moves
