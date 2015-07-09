# -*- coding: utf-8 -*-

from Location import *

class Road :
	"""Class which calcul the way to use to move a Character on the map"""

	def __init__(self, tailleX, tailleY) :
		self._list = list()
        for k in range(tailleX) :
            self._list.append(list())
            for i in range(tailleY) :
                self._list[k].append(None)
        self._tailleX=tailleX
        self._tailleY=tailleY

	def getCellPoids(self, Loc) :
		if self._list[Loc.getAbscisse()][Loc.getOrdonnee()] is None :
			return 0
		else :
			return len(self._list[Loc.getAbscisse()][Loc.getOrdonnee()])

	def getCellRoad(self, Loc) :
		return self._list[Loc.getAbscisse()][Loc.getOrdonnee()]

	def setCellRoad(self, Loc, road) :
		if format(road) != list :
			raise Exception("road n'est pas une liste")
    	self._list[Loc.getAbscisse()][Loc.getOrdonnee()] = road

    