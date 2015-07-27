import socket
import threading
import sys
sys.path.append("../tools/")
import convertBinary as cb
import File
from Battle import *

IP = ""
PORT = 10000

class ClientThread(threading.Thread) :

	def __init__(self, ip, port, clientsocket, WaitingList):
		threading.Thread.__init__(self)
		self._ip = ip
		self._port = port
		self._clientsocket = clientsocket
		self._waitingList = WaitingList
		print("[+] Nouveau thread pour %s %s" % (self.getIP(), self.getPort(), ))

	def run(self) :
		while(1) :
			r = self.getClientSocket().recv(2048)
			print(r)
			r = cb.stringBinaryToList(r)
			print(r)
			if r[0] == 0 :
				print("Client déconnecté :" + str(self.getIP())+ " " + str(self.getPort()))
				break
			if r[0] == 1 :
				self.getWaintingList().addPlayer(Player(self.getClientSocket(), self.getIP(), self.getPort()))
				self.getClientSocket().send('Waiting for an opponent')
				break

	def getWaintingList(self) :
		return self._waitingList				

	def getIP(self) :
		return self._ip

	def getPort(self) : 
		return self._port

	def getClientSocket(self) :
		return self._clientsocket




class ListThread(threading.Thread) :

	def __init__(self) :
		threading.Thread.__init__(self)
		self._list = list()

	def getList(self) :
		return self._list

	def addPlayer(self, player) :
		if not isinstance(player, Player) :
			raise Exception("player isn't a Player")
		self.getList().append(player)

	def tailleList(self) :
		return len(self.getList())

	def run(self) :
		while(1) :
			if self.tailleList() >= 2 :
				player1 = self.getList().pop(0)
				player2 = self.getList().pop(0)
				b = Battle(player1, player2)
				b.start()

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((IP,PORT))

WaitingList = ListThread()
WaitingList.start()


while True:
	tcpsock.listen(10)
	print( "En écoute...")
	(clientsocket, (ip, port)) = tcpsock.accept()
	newthread = ClientThread(ip, port, clientsocket, WaitingList)
	newthread.start()

