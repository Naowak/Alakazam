import sys

sys.path.append("../map")
from Map import *

from Capacity import *
from ListEffect import *

class Character :
	"Class which define what a Character is, all different Character will inherite from this class"

	def __init__(self, name, lifePoint, mana, mouvementPoint) :
		if not isinstance(name, str) :
			raise Exception("Name isn't a str")
		if not isinstance(lifePoint, int) :
			raise Exception("LifePoint isn't an integer")
		if not isinstance(mana, int) :
			raise Exception("Mana isn't an integer")
		if not isinstance(mouvementPoint, int) :
			raise Exception("mouvementPoint isn't an integer")

		self._name = name
		self._lifePointMax = lifePoint
		self._lifePoint = lifePoint
		self._manaMax = mana
		self._mana = mana
		self._mouvementPointMax = mouvementPoint
		self._mouvementPoint = mouvementPoint
		self._porteeBonusMalus = 0
		self._capacityList = list()
		self._listEffectBeginTurn = ListEffect()
		self._listEffectEndTurn = ListEffect()
		self._listEffectTakeDamage = ListEffect()
		self._location = None

	def __str__(self) :
		s =  str(self.getName()) + ' = Vie : ' + str(self.getLifePoint()) + '/' + str(self.getLifePointMax()) + \
		' ,  Mana : ' + str(self.getMana()) + '/' + str(self.getManaMax()) + ' , MP : ' + str(self.getMouvementPoint()) \
		+ '/' + str(self.getMouvementPointMax()) + " , PO : " + str(self.getPorteeBonusMalus()) + ' , CapacityList :' 
		for elem in self._capacityList :
			s += elem.getName()
			s += "   "
		return s

	def getName(self) :
		return self._name

	def setName(self, name) :
		if not isinstance(name, str) :
			raise Exception("Name isn't a str")
		self._name = name

	def getLifePointMax(self) :
		return self._lifePointMax

	def setLifePointMax(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		if number <= 0 :
			number = 1
		if number < self.getLifePoint() :
			self.setLifePoint(number)
		self._lifePointMax = number

	def addLifePointMax(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		self.setLifePointMax(self.getLifePointMax() + number)

	def getLifePoint(self) :
		return self._lifePoint

	def setLifePoint(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		if number < 0 :
			number = 0
		if number > self.getLifePointMax() :
			number = self.getLifePointMax()
		self._lifePoint = number

	def addLifePoint(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		self.setLifePoint(self.getLifePoint() + number)

	def isDead(self) :
		return self.getLifePoint() == 0

	def getManaMax(self) :
		return self._manaMax

	def setManaMax(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		if number < 0 :
			number = 0
		if number < self.getMana() :
			self.setMana(number)
		self._manaMax = number

	def addManaMax(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		self.setManaMax(self.getManaMax() + number)

	def getMana(self) :
		return self._mana

	def setMana(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		if number < 0 :
			number = 0
		if number > self.getManaMax() :
			number = self.getManaMax()
		self._mana = number

	def addMana(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		self.setMana(self.getMana() + number)

	def getMouvementPointMax(self) :
		return self._mouvementPointMax

	def setMouvementPointMax(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		if number < 0 :
			number = 0
		if number < self.getMouvementPoint() :
			self.setMouvementPoint(number)
		self._mouvementPointMax = number

	def addMouvementPointMax(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		self.setMouvementPointMax(self.getMouvementPointMax() + number)

	def getMouvementPoint(self) :
		return self._mouvementPoint

	def setMouvementPoint(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		if number < 0 :
			number = 0
		if number > self.getMouvementPointMax() :
			number = self.getMouvementPointMax()
		self._mouvementPoint = number

	def addMouvementPoint(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		self.setMouvementPoint(self.getMouvementPoint() + number)

	def getPorteeBonusMalus(self) :
		return self._porteeBonusMalus

	def setPorteeBonusMalus(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		self._porteeBonusMalus = number

	def addPorteeBonusMalus(self, number) :
		if not isinstance(number, int) :
			raise Exception("number isn't an int")
		self.setPorteeBonusMalus(self.getPorteeBonusMalus() + number)

	def addCapacity(self, C) :
		if not isinstance(C, Capacity) :
			raise Exception("C isn't a Capacity")
		self._capacityList.append(C)

	def removeCapacity(self, name) :
		if not isinstance(name, str) :
			raise Exception("name isn't a str")
		i = 0
		for elem in self._capacityList :
			if elem.getName() == name :
				self._capacityList.pop(i)
				return
			i += 1

	def useCapacity(self, name, Loc1, Loc2, M) :
		if not isinstance(name, str) :
			raise Exception("name isn't a str")
		if not isinstance(M, Map) :
			raise Exception("m isn't a Map")
		if M.isOut(Loc1) :
			raise Exception("Loc1 is out the Map")
		if M.isOut(Loc2) :
			raise Exception("Loc2 is out the Map")

		i = 0
		for elem in self._capacityList :
			if elem.getName() == name :
				if self.getMana() < elem.getManaCost() :
					raise Exception("Doesn't have enought mana to do it !")
				elem.use(Loc1, Loc2, M)
				self.addMana(-1*elem.getManaCost())
				return
			i += 1
		raise Exception("Character doesn't have that Capacity")

	def setCharacterOnMap(self, Loc1, M) :
		if not isinstance(M, Map) :
			raise Exception("M isn't a map")
		if not isinstance(Loc1, Location) :
			raise Exception("Loc1 isn't a Location")
		M.setCellCharacter(Loc1, self)
		self._location = Loc1

	def getLocation(self) :
		return self._location

	def setLocationToNone(self) :
		self._location = None

	def addEffectBeginTurn(self, Ef) :
		if not isinstance(Ef, Effect) :
			raise Exception("Ef isn't an Effect")
		self._listEffectBeginTurn.addEffect(Ef)

	def addEffectEndTurn(self, Ef) :
		if not isinstance(Ef, Effect) :
			raise Exception("Ef isn't an Effect")
		self._listEffectEndTurn.addEffect(Ef)

	def addEffectTakeDamage(self, Ef) :
		if not isinstance(Ef, Effect) :
			raise Exception("Ef isn't an Effect")
		self._listEffectTakeDamage.addEffect(Ef)

	def applyEffectBeginTurn(self, turn) :
		if not isinstance(turn, int) :
			raise Exception("turn isn't an integer")
		self._listEffectBeginTurn.applyEffect(turn)

	def applyEffectEndTurn(self, turn) :
		if not isinstance(turn, int) :
			raise Exception("turn isn't an integer")
		self._listEffectEndTurn.applyEffect(turn)

	def applyEffectTakeDamage(self, turn) :
		if not isinstance(turn, int) :
			raise Exception("turn isn't an integer")
		self._listEffectTakeDamage.applyEffect(turn)


