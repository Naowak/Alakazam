# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:12:50 2015

@author: Gauthier
"""
from Cell import *
from  Location import *

class Map:
	"Classe carte"
	
	def __init__(self, tailleX, tailleY):
		self._list = list()
		for k in range(tailleX) :
			self._list.append(list())
			for i in range(tailleY) :
				self._list[k].append(Cell())
		self._tailleX=tailleX
		self._tailleY=tailleY
	
	def getTailleX(self):#
		return self._tailleX
	
	def getTailleY(self):#
		return self._tailleY 
	
	def getCell(self, Loc):#
		if self.isOut(Loc):
			raise Exception("Location out of map")
		return self._list[Loc.getAbscisse()][Loc.getOrdonnee()]

	def setCell(self, C, Loc) :
		if not isinstance(C, Cell) :
			raise Exception("C isn't a Cell")
		if self.isOut(Loc) :
			raise Exception("Loc is out of Map")

		self._list[Loc.getAbscisse()][Loc.getOrdonnee()] = C
	
	def setCellType(self, Loc, strType):#
		if self.isOut(Loc):
			raise Exception("Location out of map")
		if strType=="Empty":
			self._list[Loc.getAbscisse()][Loc.getOrdonnee()].setEmpty()
		elif strType=="Full":
			self._list[Loc.getAbscisse()][Loc.getOrdonnee()].setFull()
		elif strType=="Taken":
			self._list[Loc.getAbscisse()][Loc.getOrdonnee()].setTaken()
		elif strType=="Hole":
			self._list[Loc.getAbscisse()][Loc.getOrdonnee()].setHole()
		else:
			raise Exception("strType non compris")
	
	def getCellType(self, Loc):#
		if self.isOut(Loc):
			raise Exception("Location out of map")
		if self.getCell(Loc).getType()==1:
			return "Empty"
		elif self.getCell(Loc).getType()==2:
			return "Taken"
		elif self.getCell(Loc).getType()==3:
			return "Full"
		elif self.getCell(Loc).getType()==4:
			return "Hole"
	
	def setCellCharacter(self, Loc, Char):#
		if self.isOut(Loc):
			raise Exception("Location out of map")
		self.getCell(Loc).setCharacter(Char)
	
	def getCellCharacter(self, Loc):#
		if self.isOut(Loc):
			raise Exception("Location out of map")
		return self.getCell(Loc).getCharacter()
	
	
	def isCellType(self, Loc, strType):#
		if self.isOut(Loc):
			raise Exception("Location out of map")
			
		if strType=="Empty":
			return self._list[Loc.getAbscisse()][Loc.getOrdonnee()].isEmpty()
		elif strType=="Full":
			return self._list[Loc.getAbscisse()][Loc.getOrdonnee()].isFull()
		elif strType=="Taken":
			return self._list[Loc.getAbscisse()][Loc.getOrdonnee()].isTaken()
		elif strType=="Hole":
			return self._list[Loc.getAbscisse()][Loc.getOrdonnee()].isHole()
		else:
			raise Exception("strType non compris")

	def clone(self) :
		M = Map()
		for i in range(self._tailleX) :
			for j in range(self._tailleY) :
				M._list[i][j] = self.getCell(Location(i,j)).clone()

	def switchCell(self, Loc, Loc2) :
		if self.isOut(Loc) or self.isOut(Loc2) :
			raise Exception("Location out of Map")

		C = self.getCell(Loc)
		self.setCell(self.getCell(Loc2), Loc)
		self.setCell(C, Loc2)

	def areCellsEquals(self, Loc, Loc2) :
		if self.isOut(Loc) or self.isOut(Loc2) :
			raise Exception("Loc out of Map")

		return Loc.equals(Loc2)


	def __str__(self):
		s =""
		for j in range(self.getTailleY()):
			for i in range(self.getTailleX()):
				s += str(self.getCell(Location(i,j)).getType())
				s += " "
			s += "\n"
		return s
	
	def isOut(self,Loc):#
		if not isinstance(Loc, Location) :
			raise Exception("Loc isn't a Location")

		if Loc.getAbscisse() >= self.getTailleX() or Loc.getAbscisse() < 0 or Loc.getOrdonnee() >= self.getTailleY() or Loc.getOrdonnee() < 0 :
			return True
		else:
			return False
	
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