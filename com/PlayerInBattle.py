import sys
sys.path.append("../character/")
from Team import *

class PlayerInBattle() :

	def __init__(self, player, team) :
		if not isinstance (team, Team) :
			raise Exception("team isn't a Team Object")
		self._player = player
		self._team = team

	def getPlayer(self) :
		return self._player

	def getTeam(self) :
		return self._team


