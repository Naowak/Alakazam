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

class Battle() :

	def __init__(self) :
		self._player1 = PlayerClient()
		self._player2 = PlayerClient()
		self._map = None
		self._nbPlayer = 0

	def getMap(self) :
		return self._map

	def setMap(self, M) :
		if not isinstance(M, MapClient) :
			raise Exception("M isn't a MapClient")
		self._map = M

	def getPlayer1(self) :
		return self._player1

	def setPlayer1(self, Player) :
		if not isinstance(Player, PlayerClient) :
			raise Exception("Player isn't a PlayerClient")
		self._player1 = Player

	def getPlayer2(self) :
		return self._player1

	def setPlayer2(self, Player) :
		if not isinstance(Player, PlayerClient) :
			raise Exception("Player isn't a PlayerClient")
		self._player1 = Player

	def setNbPlayer(self, nb) :
		if not isinstance(nb, int):
			raise Exception("nb isn't an int")
		self._nbPlayer = nb

	def getNbPlayer(self) :
		return self._nbPlayer


class ClientThreadReception(threading.Thread) :

	def __init__(self, ip, port, connection, ThreadSending) :
		threading.Thread.__init__(self)
		self._ip = ip
		self._port = port
		self._connection = connection
		self._continue = True
		self._threadSending = ThreadSending
		ThreadSending.setThreadReception(self)
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

	def getThreadSendind(self) :
		return self._threadSending

	def run(self) :
		while(self.getContinue()) :

			mess = self.getConnection().recv(2048)
			mess = cb.stringBinaryToList(mess)
			if(len(mess) == 1 and mess[0] == 0) :
				self.setContinue(False)
				self.getThreadSendind().setContinue(False)
				print("Deconnexion...")
			elif(len(mess) == 2 and mess[0] == 1) :
				b = Battle()
				self.setBattle(b)
				self.getThreadSendind().setBattle(b)
				self.getBattle().setNbPlayer(mess[1])
			elif(len(mess) == 1 and mess[0] == 1 and mess[1] == 1) :
				if not self.getBattle().getPlayer1().getTeam() :
					self.getBattle().Player1().setTeam(decodeTeamInit(mess[2:]))
					print(self.getBattle().Player1().getTeam())
				elif not self.getBattle().Player2().getTeam() :
					self.getBattle().Player2().setTeam(decodeTeamInit(mess[2:]))
					print(self.getBattle().Player2().getTeam())
				else :
					raise Exception("Both player have already a Team")
			elif(len(mess) > 1 and mess[0] == 2) :
				self.getBattle().setMap(MapClient(mess[1:]))
				print(self.getBattle().getMap())
			
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



