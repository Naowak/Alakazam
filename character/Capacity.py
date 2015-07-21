import sys
sys.path.append("../map")
from Map import *

class Capacity :
	"""classe servant à définir les différents sort de chaque personnage"""
	
	def __init__(self, name, fct, portee, manaCost, coolDown, lineOfSight ) :
		#A faire : ajout de la description de la Capacity
		if not isinstance(portee, int):
			raise Exception ("portee must be an integer")
		if not isinstance(coolDown, int):
			raise Exception ("coolDown must be an integer")
		if not isinstance(manaCost, int):
			raise Exception ("manaCost must be an integer")
		if not isinstance(name, str):
			raise Exception ("name must be a string")
		if not isinstance(lineOfSight, bool):
			raise Exception ("lineOfSight must be a boolean")
		if not callable(fct):
			raise Exception ("fct must be a function")
			
		self._portee=portee
		self._fct=fct
		self._coolDown=coolDown
		self._manaCost=manaCost
		self._name=name
		self._coolDownRest=0
		self._lineOfSight=lineOfSight


	def getPortee(self):
		return self._portee
		
	def getFct(self):
		return self._fct
	
	def getCoolDown(self):
		return self._coolDown
	
	def getCoolDownRest(self):
		return self._coolDownRest
	
	def getManaCost(self):
		return self._manaCost
	
	def getName(self):
		return self._name
	
	def hasLineOfSight(self):
		return self._lineOfSight
	
	def setPortee(self, portee):
		if not isinstance(portee, int):
			raise Exception("portee must be an integer")
		self._portee=portee
	
	def setFct(self, fct):
		if not callable(fct):
			raise Exception("fct must be a function")
		self._fct=fct
	
	def setCoolDown(self, coolDown):
		if not isinstance(coolDown, int):
			raise Exception("coolDown must be an integer")
		self._coolDown=coolDown
	
	def setCoolDownrest(self, coolDownRest):
		if not isinstance(coolDownRest, int):
			raise Exception("coolDownRest must be an integer")
		self._coolDownRest=coolDownRest
		
	def setManaCost(self, manaCost):
		if not isinstance(manaCost, int):
			raise Exception("manaCost must be an integer")
		self._manaCost=manaCost
	
	def setName(self, name):
		if not isinstance(name, str):
			raise Exception("name must be a string")
		self._name=name
	
	def setLineOfSight(self, lineOfSight):
		if not isinstance(lineOfSight, bool):
			raise Exception("lineOfSight must be a boolean")
		self._lineOfSight=lineOfSight
	
	def use(self, LocThrower, LocTarget, M):
		if M.isOut(LocThrower):
			raise Exception ("LocTrower out of Map")
		if M.isOut(LocTarget):
			raise Exception ("LocTarget out of Map")
			
		return self.getFct()(LocThrower,LocTarget)