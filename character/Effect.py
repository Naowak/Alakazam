import sys
sys.path.append("../map")
from Map import *
sys.path.append("../character")

class Effect :
	"""Classe rassemblant les differents effets pouvant s'appliquer sur un perso, non debuffables"""
	
	def __init__(self, name, fct, listTurn, Thrower, Target):
		#A faire : ajout de la description de l'effet
		if not isinstance(name, str):
			raise Exception ("name must be a string")
		if not callable(fct):
			raise Exception ("fct must be a function")
		if not isinstance(listTurn, list):
			raise Exception ("listTurn must be a list")
		for k in listTurn:
			if not isinstance(k, int):
				raise Exception ("listTurn must be a list of integers")
		#if not isinstance(Thrower, Character) :
			#raise Exception("Thrower isn't a Character")
		#if not isinstance(Target, Character) :
			#raise Exception("Target isn't a Character")
		
		#le principe de listTrun est de stocker les tours pendant lesquels l'effet va etre actif
		#si l'effet debute dans 2 tours pour 3 tours la liste sera [tour+2,tour+3,tour+4]
		
		#type 1 - buff : Bonus/malus recu au lancement du sort pour un nombre de tours limite
		#type 2 - timeEffect : effet active a chaque tour pendant un nombre de tours donne
		#type 0 - effet : non debuffable
		
		self._name=name
		self._fct=fct
		self._listTurn=listTurn[:]
		self._thrower = Thrower
		self._target = Target
		
		
	def getName(self):
		return self._name
	
	def getFct(self):
		return self._fct
	
	def getListTurn(self):
		return self._listTurn

	def getThrower(self) :
		return self._thrower

	def getTarget(self) :
		return self._target

	def removeTurnFromList(self, turn) :
		#not usefull for the moment, maybe later
		if not isinstance(turn, int) :
			raise Exception("turn isn't an integer")
		self._listTurn = [value for value in self._listTurn if value != turn]
	
	def setName(self, name):
		if not isinstance(name, str):
			raise Exception ("name muste be a string")
		self._name=name
	
	def setFct(self, fct):
		if not callable(fct):
			raise Exception ("fct must be a callable object")
		self._fct=fct
	
	def setListTurn(self, listTurn):
		if not isinstance(listTurn, list):
			raise Exception ("listTurn must be a list")
		for k in listTurn:
			if not isinstance(k, int):
				raise Exception ("listTurn must be a list of integers")
		self._listTurn=listTurn[:]

	def isListTurnEmpty(self) :
		return len(self._listTurn) == 0

	def setThrower(self, Thrower) :
		#if not isinstance(Thrower, Character) :
			#raise Exception("Thrower isn't a Character")
		self._thrower = Thrower

	def setTarget(self, Target) :
		#if not isinstance(Target, Character) :
			#raise Exception("Target isn't a Character")
		self._target = Target
	
	def use(self):
		self.getListTurn().pop(0)
		return self.getFct()(self.getThrower(), self.getTarget())
	
	def debuff(self):
		pass