class Location :

	""" Coordonnées utilisées pour accéder aux Cells"""

	def __init__(self, x, y) :
		self._x = x
		self._y = y

	def getAbcsisse(self) :
		return self._x

	def getOrdonnee(self) :
		return self._y

	def setAbscisse(self, x) :
		self._x = x

	def setOrdonnee(self, y) :
		self._y = y

	def equals(self, loc) :
		return self.getAbcsisse() == loc.getAbcsisse() and self.getOrdonnee() == loc.getOrdonnee()

	def clone(self) :
		return Location(self.getAbcsisse(), self.getOrdonnee())

	def __str__(self) :
		return '[' + str(self._x) + " : " + str(self._y) + ']'