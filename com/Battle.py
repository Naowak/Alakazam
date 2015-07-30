import Thread
from PlayerInBattle import *
import sys
sys.path.append("../map/")
from Map import *

TAILLE_MAP_X = 30
TAILLE_MAP_Y = 30

class Battle(threading.Thread) :

	def __init__(self, playerInBattle1, playerInBattle2) :
		if not isinstance(playerInBattle1, PlayerInBattle) :
			raise Exception("playerInBattle1 isn't a PlayerInBattle")
		if not isinstance(playerInBattle2, PlayerInBattle) :
			raise Exception("playerInBattle2 isn't a PlayerInBattle")

		self._playerInBattle1 = playerInBattle1
		self._playerInBattle2 = playerInBattle2
		self._map = Map(TAILLE_MAP_X, TAILLE_MAP_Y)

	def getPlayerInBattle1(self) :
		return self._playerInBattle1

	def getPlayerInBattle2(self) :
		return self._playerInBattle2

	def getListPlayerInBattle(self) :
		return [self.getPlayerInBattle1(), self.getPlayerInBattle2()]

	def getMap(self) :
		return self._map
