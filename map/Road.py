# -*- coding: utf-8 -*-

import sys
sys.path.append("../tools")

from Location import *
from File import *

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
		if not isinstance(Loc, Location) :
			raise Exception("Loc isn't a Location")
		return Loc.getAbscisse() >= self.getTailleX() or Loc.getOrdonnee() >= self.getTailleY() or Loc.getAbscisse() < 0 or Loc.getOrdonnee()< 0

	def getUpLeft(self, Loc):
		if self.isOut(Loc):
			raise Exception("Location out of map")
		
		Loc2=Location(Loc.getAbscisse()-1 if Loc.getOrdonnee()%2==0 else Loc.getAbscisse(),Loc.getOrdonnee()-1)
		if self.isOut(Loc2):
			return None
		else:
			return Loc2
            

	def getUpRight(self, Loc):
		if self.isOut(Loc):
			raise Exception("Location out of map")
		Loc2 = Location(Loc.getAbscisse()+1 if Loc.getOrdonnee()%2==1 else Loc.getAbscisse(),Loc.getOrdonnee()-1)
		if self.isOut(Loc2):
			return None
		else:
			return Loc2

	def getRight(self, Loc):
		if self.isOut(Loc):
			raise Exception("Location out of map")
		
		Loc2 = Location(Loc.getAbscisse()+1,Loc.getOrdonnee())
		if self.isOut(Loc2):
			return None
		else:
			return Loc2
	
	def getLeft(self, Loc):
		if self.isOut(Loc):
			raise Exception("Location out of map")
		
		Loc2 = Location(Loc.getAbscisse()-1,Loc.getOrdonnee())
		if self.isOut(Loc2):
			return None
		else:
			return Loc2
			
		
	def getDownLeft(self, Loc):
		if self.isOut(Loc):
			raise Exception("Location out of map")
		
		Loc2=Location(Loc.getAbscisse()-1 if Loc.getOrdonnee()%2==0 else Loc.getAbscisse(),Loc.getOrdonnee()+1)
		if self.isOut(Loc2):
			return None
		else:
			return Loc2
	
	def getDownRight(self, Loc):
		if self.isOut(Loc):
			raise Exception("Location out of map")
		
		Loc2=Location(Loc.getAbscisse() if Loc.getOrdonnee()%2==0 else Loc.getAbscisse()+1,Loc.getOrdonnee()+1)
		if self.isOut(Loc2):
			return None
		else:
			return Loc2

	def getCellListeVoisins(self, Loc) :
		if self.isOut(Loc) :
			raise Exception("Location out of Map")

		L = list()

		gUR = self.getUpRight(Loc)
		if gUR != None :
			L += [gUR]

		gR = self.getRight(Loc)
		if gR != None :
			L += [gR]

		gDR = self.getDownRight(Loc)
		if gDR != None :
			L += [gDR]

		gDL = self.getDownLeft(Loc)
		if gDL != None :
			L += [gDL]

		gL = self.getLeft(Loc)
		if gL != None :
			L += [gL]

		gUL = self.getUpLeft(Loc)
		if gUL != None :
			L += [gUL]

		return L

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

	def initializeRoadCellToNone (self, Loc) :
		if self.isOut(Loc) :
			raise Exception("Location out of the Map")
		self._list[Loc.getAbscisse()][Loc.getOrdonnee()] = None

	def initializeRoadAllCells(self) :
		for i in range(self.getTailleX()) :
			for j in range(self.getTailleY()) :
				self.initializeRoadCellToNone(Location(i,j))

	def findRoadsForCells(self, max, Loc) :
		if self.isOut(Loc) :
			raise Exception("Location out of the Map")
		if not isinstance(max, int) :
			raise Exception("Max n'est pas un int")

		self.initializeRoadAllCells()
		self.setCellRoad(Loc, [Loc])
		F = File()
		F.enfiler(Loc)

		while self.getCellPoids(Loc) < max + 1 and not F.fileVide() :
			for Loc2 in self.getCellListeVoisins(Loc) :
				if self.getCellPoids(Loc2) > self.getCellPoids(Loc) + 1 or self.getCellPoids(Loc2) == 0 :
					self.setCellRoad(Loc2, self.getCellRoad(Loc) + [Loc2])
					F.enfiler(Loc2)
			Loc = F.getValeur()
			F.defiler()





