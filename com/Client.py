import socket
import threading
import sys
sys.path.append("../tools/")
import convertBinary as cb
sys.path.append("../map/")
from MapClient import *
from EncodeDecodeClient import *
from PlayerClient import *

IP = ""
PORT = 10000

class ClientThreadReception(threading.Thread) :

	def __init__(self, ip, port, connection, ThreadSending) :
		threading.Thread.__init__(self)
		self._ip = ip
		self._port = port
		self._connection = connection
		self._continue = True
		self._threadSending = ThreadSending
		ThreadSending.setThreadReception(self)

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

	def getThreadSendind(self) :
		return self._threadSending

	def run(self) :
		while(self.getContinue()) :

			mess = self.getConnection().recv(2048)
			mess = cb.stringBinaryToList(mess)
			if(mess[0] == 0) :
				self.setContinue(False)
				self.getThreadSendind().setContinue(False)
				print("Deconnexion...")
			elif(mess[0] == 1) :
				Player1 = PlayerClient()
				Player2 = PlayerClient()
			elif(mess[0] == 2) :
				M = MapClient(mess[1:])
				print(M)
			elif(mess[0] == 3) :
				if not Player1.getTeam() :
					Player1.setTeam(decodeTeamInit(mess[1:]))
					print(Player1.getTeam())
				elif not Player2.getTeam() :
					Player2.setTeam(decodeTeamInit(mess[1:]))
					print(Player2.getTeam())
				else :
					raise Exception("Both player have already a Team")
			else :
				print(mess)



class ClientThreadSending(threading.Thread) :

	def __init__(self, ip, port, connection) :
		threading.Thread.__init__(self)
		self._ip = ip
		self._port = port
		self._connection = connection
		self._continue = True
		self._threadReception = None

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
			#if(mess.decode() == '0') :
			#	self.getThreadReception().setContinue(False)
			#	self.setContinue(False)
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



