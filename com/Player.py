import socket
import sys
sys.path.append("../tools/")
import convertBinary as cb
sys.path.append("../character/")
from Team import *

class Player :
	"""define a Player"""

	def __init__(self, referenceSocket, ip, port, listToDecode) :
		if not isinstance(listToDecode, list) :
			raise Exception("listToDecode isn't a list Object")
		self._referenceSocket = referenceSocket
		self._ip = ip
		self._port = port
		self._team = listToDecode

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

	def getTeam(self) :
		return self._team

	def setTeam(self, team) :
		if not isinstance(team, Team) :
			raise Exception("team ins't a Team Object")
		self._team = team