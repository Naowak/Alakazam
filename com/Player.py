import socket
import sys
sys.path.append("../tools/")
import convertBinary as cb
from PlayerInBattle import *
sys.path.append("../character/")
from Team import *

class Player :
	"""define a Player"""

	def __init__(self, referenceSocket, ip, port) :
		self._referenceSocket = referenceSocket
		self._ip = ip
		self._port = port
		self._playerInBattle = None

	def getReferenceSocket(self) :
		return self._referenceSocket

	def getIP(self) :
		return self._ip

	def getPort(self) :
		return self._port

	def sendToPlayer(self, mess) :
		if not isinstance(mess, bytes) :
			raise Exception("mess isn't a byte")
		self.getReferenceSocket().send(mess.encode())

	def recvFromPlayer(self) :
		mess = self.getReferenceSocket().recv(2048)
		return mess.decode()

	def initPlayerInBattle(self, team) :
		if not isinstance(team, Team) :
			raise Exception("team isn't a Team Object")
		self._playerInBattle = PlayerInBattle(self, team)

	def getPlayerInBattle(self) :
		return self._playerInBattle

	def setPlayerInBattle(self, PIB) :
		if not isinstance(PIB, PlayerInBattle) :
			raise Exception("PIB isnt a PlayerInBattle")
		self._playerInBattle = PIB