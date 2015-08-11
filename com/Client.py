import socket
import threading
import sys
sys.path.append("../tools/")
import convertBinary as cb
sys.path.append("../map/")
from EncodeDecodeClient import *

IP = ""
PORT = 10000


class ClientThreadReception(threading.Thread) :

	def __init__(self, ip, port, connection, ThreadSending) :
		threading.Thread.__init__(self)
		self._ip = ip
		self._port = port
		self._connection = connection
		self._continue = True
		self._Battle = None
		self._threadSending = ThreadSending
		ThreadSending.setThreadReception(self)

	def getBattle(self) :
		return self._Battle

	def setBattle(self, battle) :
		if not isinstance(battle, Battle) :
			raise Exception("battle isn't a Battle")
		self._Battle = battle

	def getIP(self) :
		return self._IP

	def getPort(self) :
		return self._port

	def getConnection(self) :
		return self._connection

	def getContinue(self) :
		return self._continue

	def setContinue(self, b) :
		if not isinstance(b, bool) :
			raise Exception("b isn't a boolean")
		self._continue = b

	def sendMessage(self, mess) :
		if isinstance(mess, list) :
			mess = listToStringBinary(mess)
		else :
			mess = mess.encode()
		sendRequest(self.getConnection(), mess)

	def deleteBattle(self) :
		self._Battle = None

	def getThreadSending(self) :
		return self._threadSending

	def run(self) :
		#self.sendMessage("1 1")

		while(self.getContinue()) :

			mess = self.getConnection().recv(2048)
			mess = cb.stringBinaryToList(mess)
			messReturn = decodeMessClient(self, mess)
			if messReturn == None :
				pass

class ClientThreadSending(threading.Thread) :

	def __init__(self, ip, port, connection) :
		threading.Thread.__init__(self)
		self._ip = ip
		self._port = port
		self._connection = connection
		self._continue = True
		self._threadReception = None
		self._Battle = None

	def getBattle(self) :
		return self._Battle

	def setBattle(self, battle) :
		if not isinstance(battle, Battle) :
			raise Exception("battle isn't a Battle")
		self._Battle = battle

	def getIP(self) :
		return self._IP

	def getPort(self) :
		return self._port

	def getConnection(self) :
		return self._connection

	def getContinue(self) :
		return self._continue

	def setContinue(self, b) :
		if not isinstance(b, bool) :
			raise Exception("b isn't a boolean")
		self._continue = b

	def getThreadReception(self) :
		return self._threadReception

	def setThreadReception(self, ThreadReception) :
		if not isinstance(ThreadReception, ClientThreadReception) :
			raise Exception("ThreadReception isnt a ClientThreadReception")
		self._threadReception = ThreadReception

	def run(self) :
		while(self.getContinue()) :
			mess = demandeTexteToBinary()
			sendRequest(self._connection, mess)


def connectionToServer() :
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP, PORT))
	return s

def demandeTexteToBinary() :
	string = input(">> ")
	return string.encode()

def sendRequest(s, r) :
	if not isinstance(r, bytes) :
		raise Exception("r ins't bytes")
	if not isinstance(s, socket.socket) :
		raise Exception("s isn't a socket")
	s.send(r)

s = connectionToServer()

ThreadSending = ClientThreadSending(IP, PORT, s)
ThreadReception = ClientThreadReception(IP, PORT, s, ThreadSending)

ThreadReception.start()
ThreadSending.start()



