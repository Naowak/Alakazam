# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:22:38 2015

@author: Gauthier
"""

import sys
sys.path.append("../character")

from Character import *

class Cell :
    
    """Cellule composant la map"""
    
    def __init__(self):
        self._type=1
        self._character=None
        
    def setType(self, nb):
        if nb>0 and nb<5:
            self._type=nb
        else:
            raise Exception("nb must be between 1 and 4 include")
            
    def setCharacter(self, C):
        if not isinstance(C, Character) :
            raise Exception("C isn't a Character")
        self._character=C
        
    def getType(self):
        return self._type
    
    def getCharacter(self):
        return self._character
    
    def clone(self):
        NewCell=Cell()
        NewCell.setType(self.getType())
        NewCell.setCharacter(self.getCharacter().clone())
        return NewCell
        
    def isEmpty(self):
        return self._type==1
        
    def isTaken(self):
        return self._type==2
    
    def isFull(self):
        return self._type==3
    
    def isHole(self):
        return self._type==4
        
    def __str__(self):
        return str(self.getType()) + " : " + str(self.getCharacter())
        
    def setEmpty(self):
        self._type=1
    
    def setTaken(self):
        self._type=2
    
    def setFull(self):
        self._type=3
    
    def setHole(self):
        self._type=4