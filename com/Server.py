import socket
import threading
import sys
sys.path.append("../tools/")
import convertBinary as cb
import File
from Player import *

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
		b = True
		while(b) :
			r = self.getClientSocket().recv(2048)
			print(r)
			r = cb.stringBinaryToList(r)
			print(r)
			if r[0] == 0 :
				print("Client déconnecté :" + str(self.getIP())+ " " + str(self.getPort()))
				self.getClientSocket().send("0 0".encode())
				self.getClientSocket().close()
				b = False
			elif r[0] == 1 :
				self.getWaitingList().addPlayer(Player(self.getClientSocket(), self.getIP(), self.getPort()))
				self.getClientSocket().send('Waiting for an opponent'.encode())
				b = False

	def getWaitingList(self) :
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
				b = Battle(player1, player2, self)
				b.start()

class Battle(threading.Thread) :

	def __init__(self, player1, player2, WaitingList) :
		threading.Thread.__init__(self)
		if not isinstance(player1, Player) :
			raise Exception("player1 isn't a Player")
		if not isinstance(player2, Player) :
			raise Exception("player2 isn't a Player")
		if not isinstance(WaitingList, ListThread) :
			raise Exception("WaitingList isn't a ListThread")

		self._player1 = player1
		self._player2 = player2
		self._waitingList = WaitingList

	def getPlayer1(self) :
		return self._player1

	def getPlayer2(self) :
		return self._player2

	def getWaitingList(self) :
		return self._waitingList

	def run(self) :
		self.getPlayer1().getReferenceSocket().send("Joueur 1.".encode())
		self.getPlayer2().getReferenceSocket().send("Joueur 2.".encode())
		tab = [self.getPlayer1(), self.getPlayer2()]
		t1 = ThreadForPlayer(self.getPlayer1(), tab, self.getWaitingList())
		t2 = ThreadForPlayer(self.getPlayer2(), tab, self.getWaitingList())
		t1.start()
		t2.start()


class ThreadForPlayer(threading.Thread) :

	def __init__(self, P, tabPlayer, WaitingList) :
		threading.Thread.__init__(self)
		if not isinstance(tabPlayer, list) :
			raise Exception("tabPlayer isn't a list")
		if not isinstance(P, Player) :
			raise Exception("P isn't a Player")
		if not isinstance(WaitingList, ListThread) :
			raise Exception("WaitingList isn't a ListThread")
		self._tabPlayer = tabPlayer
		self._Player = P
		self._waitingList = WaitingList

	def getTabPlayer(self) :
		return self._tabPlayer

	def getPlayer(self) :
		return self._Player

	def getWaitingList(self) :
		return self._waitingList

	def run(self) :
		b = True
		while(b) :
			r = self.getPlayer().getReferenceSocket().recv(2048)
			if(r.decode() == '0') :
				b = False
				newthread = ClientThread(self.getPlayer().getIP(), self.getPlayer().getPort(), self.getPlayer().getReferenceSocket(), self.getWaitingList())
				newthread.start()
				for player in self.getTabPlayer() :
					if player != self.getPlayer() :
						player.getReferenceSocket().send("Oh, votre adversaire est parti ! ...".encode())
			else :
				for player in self.getTabPlayer() :
					player.getReferenceSocket().send(r)

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

