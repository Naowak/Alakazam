from Effect import *

class ListEffect :
	"""Class which contains all the function for the list of effect that can have a Character"""

	def __init__(self) :
		self._list = list()

	def addEffect(self, Ef) :
		if not isinstance(Ef, Effect) :
			raise Exception("Ef isn't an Effect !")
		self._list.append(Ef)

	def applyEffect(self, turn) :
		if not isinstance(turn, int) :
			raise Exception("turn isn't an integer")

		for elem in self._list :
			if elem.getListTurn()[0] == turn :
				elem.use()
		self.removeEffectFinishedFromList()

	def removeEffectFinishedFromList(self) :
		for elem in self._list :
			if elem.isListTurnEmpty() :
				self._list.remove(elem)

	def removeEffect(self, name) :
		#Not usefull for the moment, work with the name, maybe should work with an instance
		if not isinstance(name, str) :
			raise Exception("name isn't a str")
		for elem in self._list :
			if elem.getName() == name :
				self._list.remove(elem)


