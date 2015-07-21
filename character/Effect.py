import sys
sys.path.append("../map")
from Map import *
sys.path.append("../character")
from Character import *

class Effect :
	"""Classe rassemblant les differents effets pouvant s'appliquer sur un perso, non debuffables"""
	
	def __init__(self, name, fct, listTurn):
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
		
		#le principe de listTrun est de stocker les tours pendant lesquels l'effet va etre actif
		#si l'effet debute dans 2 tours pour 3 tours la liste sera [tour+2,tour+3,tour+4]
		
		#type 1 - buff : Bonus/malus recu au lancement du sort pour un nombre de tours limite
		#type 2 - timeEffect : effet active a chaque tour pendant un nombre de tours donne
		#type 0 - effet : non debuffable
		
		self._name=name
		self._fct=fct
		self._listTurn=listTurn[:]
		
		
	def getName(self):
		return self._name
	
	def getFct(self):
		return self._fct
	
	def getListTurn(self):
		return self._listTurn
	
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
	
	def use(self, Thrower, Target):
		if not isinstance(Thrower, Character):
			raise Exception ("Thrower must be a Character")
		if not isinstance(Target, Character):
			raise Exception ("Target must be a Character")
		self.getListTurn().pop(0)
		return self.getFct()(Thrower, Target)
	
	def debuff(self):
		pass