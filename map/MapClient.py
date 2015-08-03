# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:12:50 2015

@author: Gauthier
"""

from Cell import *
from Location import *
from random import random, choice

class MapClient:
	"Classe carte"
	
	def __init__(self, tab):
		if not isinstance(tab, list) :
			raise Exception("tab is not a list")
		
		self._list = list()
		compteur = 2
		for k in range(tab[0]) :
			self._list.append(list())
			for i in range(tab[1]) :
				self._list[k].append(Cell())
				self._list[k][i].setType(tab[compteur])
				compteur += 1
		self._tailleX=tab[0]
		self._tailleY=tab[1]	
		
	
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
		self.setCellType(Loc, "Taken")
	
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
		M = Map(self.getTailleX, self.getTailleY)
		for i in range(self.getTailleX) :
			for j in range(self.getTailleY) :
				M.setCell(self.getCell(Location(i,j)).clone(), Location(i,j))

	def switchCell(self, Loc, Loc2) :
		if self.isOut(Loc) :
			raise Exception("Loc out of Map")
		if self.isOut(Loc2) :
			raise Exception("Loc2 out of Map")

		C = self.getCell(Loc)
		self.setCell(self.getCell(Loc2), Loc)
		self.setCell(C, Loc2)

	def areCellsEquals(self, Loc, Loc2) :
		if self.isOut(Loc) :
			raise Exception("Loc out of Map")
		if self.isOut(Loc2) :
			raise Exception("Loc2 out of Map")

		return Loc.equals(Loc2)


	def __str__(self):
		s =""
		for j in range(self.getTailleY()):
			if j % 2 == 1 :
				s += " "
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
	
	def generationRelief(self) :
		for X in range( 1, self.getTailleX()-1 ) :
			for Y in range(1, (self.getTailleY()-1) // 2 ) :
				r = random()
				if r < 0.075 :
					self.setCellType(Location (X, Y), 'Full')
					self.setCellType(Location (self.getTailleX()-1-X, self.getTailleY()-1-Y), 'Full')
				elif r > 0.925 :
					self.setCellType(Location(X,Y),'Hole')
					self.setCellType(Location (self.getTailleX()-1-X, self.getTailleY()-1-Y), 'Hole')
	
	def CellsForCharacters(self):
		"Apres creation du relief, renvoie deux listes de coordonnees pour que les joueurs puissent placer leurs characters"
		L=[]
		for X in range (self.getTailleX() ) :
			for Y in range( self.getTailleY()//2 ) :
				if self.isCellType(Location(X, Y), 'Empty'):
					L+=[Location(X,Y)]
		L1=[]
		L2=[]
		for k in range (7):
			c= choice(L)
			L.remove(c)
			L1+=[c]
			L2+=[Location(self.getTailleX()-1-c.getAbscisse(), self.getTailleY()-1-c.getOrdonnee())]
			
		return [L1,L2]
			
			