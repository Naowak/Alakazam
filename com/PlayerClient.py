import sys
sys.path.append("../character")
from Team import *

class PlayerClient :

	def __init__(self) :
		self._t = None

	def getTeam(self) :
		return self._t

	def setTeam(self, team) :
		self._t = team