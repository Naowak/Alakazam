# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:12:50 2015

@author: Gauthier
"""
import Cell, Location

class Map:
    "Classe carte"
    
    def __init__(self, tailleX, tailleY):
        self._list = list()
        for k in range(tailleX) :
            self._list.append(list())
            for i in range(tailleY) :
                self._list[k].append(Cell.Cell())
        self._tailleX=tailleX
        self._tailleY=tailleY
        
    
        
    def getCell(self, Loc):
        return self._list[Loc.getAbscisse()][Loc.getOrdonnee()]
    