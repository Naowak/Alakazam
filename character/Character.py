from Capacity import *

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
		self._listEffectBeginTurn = list()
		self._listEffectEndTurn = list()
		self._listEffectTakeDamage = list()

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