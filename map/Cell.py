# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:22:38 2015

@author: Gauthier
"""

class Cell :
    
    """Cellule composant la map"""
    
    def __init__(self):
        self._type=1
        self._character=None
        
    def setType(self, nb):
        if nb>0 and nb<5:
            self._type=nb
        else:
            print("entre 1&4")
            
    def setCharacter(self, Character):
        self._character=Character
        
    def getType(self):
        return self._type
    
    def getCharacter(self):
        return self._character
    
    def clone(self):
        NewCell=Cell()
        NewCell.setType(self._type)
        #NewCell.setCharacter(self._character.clone())
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
        return str(self._type) + " : " + str(self._character)
        
    def setEmpty(self):
        self._type=1
    
    def setTaken(self):
        self._type=2
    
    def setFull(self):
        self._type=3
    
    def setHole(self):
        self._type=4