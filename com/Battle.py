import threading
import socket
from PlayerInBattle import *
import sys
sys.path.append("../map/")
from Map import *

TAILLE_MAP_X = 30
TAILLE_MAP_Y = 30

class reception

class Battle(threading.Thread) :

	def __init__(self, playerInBattle1, playerInBattle2) :
		threading.Thread.__init__(self)
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

	def testGameOver(self) :
		return testPlayer1Loose() or testPlayer2Loose()

	def testEquality(self) :
		return testPlayer1Loose() and testPlayer2Loose()

	def testPlayer1Loose(self) :
		for elem in self.getPlayerInBattle1().getTeam().getListChar() :
			if not elem.isDead() :
				return False
		return True

	def testPlayer2Loose(self) :
		for elem in slef.getPlayerInBattle2().getTeam().getListChar() :
			if not elem.isDead() :
				return False
		return True

	def run(self) :
		turn = 0
		while(not testGameOver()) :
			turnOver = False
			while(not turnOver) :



