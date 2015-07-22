# -*- coding: utf-8 -*-

from Location import *
from Map import *

class Sight :
	"""Class permettant de connaitre les lignes de vues de toutes les Cells en fonction d'une Location donnée"""

	def __init__(self, sizeX, sizeY) :
		if not isinstance(sizeX, int) :
			raise Exception("sizeX is not an integer")
		if not isinstance(sizeY, int) :
			raise Exception("sizeY is not an integer")

		self._sizeX = sizeX
		self._sizeY = sizeY
		self._list = list()

		for i in range(sizeX) :
			self._list.append(list())
			for j in range(sizeY) :
				self._list[i].append(True)

	def getSizeX(self) :
		return self._sizeX

	def getSizeY(self) :
		return self._sizeY

	def isOut(self, Loc) :
		if not isinstance(Loc, Location) :
			raise Exception("Loc isn't a Location")
		return Loc.getAbscisse() >= self.getSizeX() or Loc.getOrdonnee() >= self.getSizeY() or Loc.getAbscisse() < 0 or Loc.getOrdonnee()< 0

	def getNextCell(self, i, j, Loc) :
		if not isinstance(i, int) :
			raise Exception("i isn't an integer")
		if not isinstance(j, int) :
			raise Exception("j isn't an integer")
		if self.isOut(Loc) :
			raise Exception("Loc out of the map")

		if i == -1 and j == -1 :
			return Location(Loc.getAbscisse()-1 if Loc.getOrdonnee()%2==0 else Loc.getAbscisse(),Loc.getOrdonnee()-1)
		if i == -1 and j == 1 :
			return Location(Loc.getAbscisse()-1 if Loc.getOrdonnee()%2==0 else Loc.getAbscisse(),Loc.getOrdonnee()+1)
		if i == 0 and j == -1 :
			return Location(Loc.getAbscisse()-1,Loc.getOrdonnee())
		if i == 0 and j == 1 :
			return Location(Loc.getAbscisse()+1,Loc.getOrdonnee())
		if i == 1 and j == -1 :
			return Location(Loc.getAbscisse()+1 if Loc.getOrdonnee()%2==1 else Loc.getAbscisse(),Loc.getOrdonnee()-1)
		if i == 1 and j == 1 :
			return Location(Loc.getAbscisse() if Loc.getOrdonnee()%2==0 else Loc.getAbscisse()+1,Loc.getOrdonnee()+1)
		else :
			raise Exception("i or j isn't/aren't equals to -1/0/+1")

	def getSightCell(self, Loc) :
		if self.isOut(Loc) :
			raise Exception("Location out of the map")
		return self._list[Loc.getAbscisse()][Loc.getOrdonnee()]

	def setSightCell(self, Loc, boolean) :
		self._list[Loc.getAbscisse()][Loc.getOrdonnee()] = boolean

	def drawLine(self, Loc1, Loc2) :
		if self.isOut(Loc1) :
			raise Exception("Location1 out of the map")
		if self.isOut(Loc2) :
			raise Exception("Location2 out of the map")

		liste = list()

		deltaX = 2*(Loc2.getAbscisse() - Loc1.getAbscisse()) + abs(Loc2.getOrdonnee() % 2) - abs(Loc1.getOrdonnee() % 2)
		deltaY = Loc2.getOrdonnee() - Loc1.getOrdonnee()

		xSign = -1 if deltaX < 0 else 1
		ySign = -1 if deltaY < 0 else 1

		gammaX = abs(deltaX)
		gammaY = abs(deltaY)

		currentLoc = Loc1
		liste.append(Loc1)
		epsilon = -2*gammaX
		while not currentLoc.equals(Loc2) :
			if epsilon >= 0 :
				currentLoc = self.getNextCell(-1*xSign, ySign, currentLoc)
				epsilon = epsilon - 3*gammaX -3*gammaY
			else :
				epsilon += 3*gammaY
				if epsilon > -1*gammaX :
					currentLoc = self.getNextCell(xSign, ySign, currentLoc)
					epsilon -= 3*gammaX
				else :
					if epsilon < -3*gammaX :
						currentLoc = self.getNextCell(xSign, -1*ySign, currentLoc)
						epsilon += 3*gammaX
					else :
						currentLoc = self.getNextCell(0, xSign, currentLoc)
						epsilon += 3*gammaY
			if self.isOut(currentLoc) :
				raise Exception("CurrentLoc out of map")
			liste.append(currentLoc)

		return liste

	def fieldOfView(self, Loc, M) :
		if self.isOut(Loc) :
			raise Exception("Loc out of the map")
		if not isinstance(M, Map) :
			raise Exception("M isn't a Map")

		for i in range(self.getSizeX()) :
			for j in range(self.getSizeY()) :
				k = 0
				line = self.drawLine(Loc, Location(i,j))
				kMax = len(line) - 1
				for elem in line :
					if M.getCellType(elem) == "Full" or (M.getCellType(elem) == "Taken" and k != 0 and k != kMax):
						self.setSightCell(Location(i,j), False)
						break
					k += 1

	def string(self, Loc, M) :
		s = ""
		for j in range(self.getSizeY()) :
			if j % 2 == 1 :
				s = s + " "
			for i in range(self.getSizeX()) :
				if i == Loc.getAbscisse() and j == Loc.getOrdonnee() :
					s = s + "C "
				elif M.getCellType(Location(i,j)) == "Taken" or M.getCellType(Location(i,j)) == "Full" :
					s = s + "M "
				elif self.getSightCell(Location(i,j)) == True :
					s = s + "_ "
				else :
					s = s + "  "
			s = s + "\n"
		return s




