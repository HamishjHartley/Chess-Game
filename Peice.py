import numpy as np

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
