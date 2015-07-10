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

	def getTailleX(self) :
		return self._tailleX

	def getTailleY(self) :
		return self._tailleY

	def isOut(self, Loc) :
		return Loc.getAbscisse() >= self.getTailleX() or Loc.getOrdonnee() >= self.getTailleY() or Loc.getAbscisse() < 0 or Loc.getOrdonnee()< 0

	def getCellPoids(self, Loc) :
		if self.isOut(Loc) :
			raise Exception("Location out of the map")

		if self._list[Loc.getAbscisse()][Loc.getOrdonnee()] is None :
			return 0
		else :
			return len(self._list[Loc.getAbscisse()][Loc.getOrdonnee()])

	def getCellRoad(self, Loc) :
		if self.isOut(Loc) :
			raise Exception("Location out of the map")
		
		return self._list[Loc.getAbscisse()][Loc.getOrdonnee()]

	def setCellRoad(self, Loc, road) :
		if self.isOut(Loc) :
			raise Exception("Location out of the map")
		
		if not isinstance(road, list) :
			raise Exception("road n'est pas une liste")
		for elem in road :
			if not isinstance(elem, Location) :
				raise Exception("Un élément de la liste n'est pas une Location")
		self._list[Loc.getAbscisse()][Loc.getOrdonnee()] = road



    
