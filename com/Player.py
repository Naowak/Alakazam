import socket
import sys
sys.path.append("../tools/")
import convertBinary as cb

class Player :
	"""define a Player"""

	def __init__(self, referenceSocket, ip, port) :
		self._referenceSocket = referenceSocket
		self._ip = ip
		self._port = port

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