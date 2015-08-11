import socket
import threading
import sys
sys.path.append("../tools/")
import convertBinary as cb
import File
from Player import *
from DecodeEncodeServer import *
sys.path.append("../map/")
from Map import *

TAILLE_MAP_X = 30
TAILLE_MAP_Y = 30


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
			#self.getClientSocket().send("Connected to Server".encode())
			r = self.getClientSocket().recv(2048)
			print(r)
			r = cb.stringBinaryToList(r)
			print(r)
			if r[0] == 0 :
				print("Client déconnecté :" + str(self.getIP())+ " " + str(self.getPort()))
				self.getClientSocket().send("0".encode())
				self.getClientSocket().close()
				b = False
			elif r[0] == 1 :
				self.getWaitingList().addPlayer(Player(self.getClientSocket(), self.getIP(), self.getPort(), r[1:]))
				#self.getClientSocket().send('Waiting for an opponent'.encode())
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
				b = Room(player1, player2, self)
				b.start()

class Room(threading.Thread) :

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
		self._map = Map(TAILLE_MAP_X, TAILLE_MAP_Y)
		self._waitingList = WaitingList

	def getPlayer1(self) :
		return self._player1

	def getPlayer2(self) :
		return self._player2

	def getWaitingList(self) :
		return self._waitingList

	def getMap(self) :
		return self._map

	def testPlayerLoose(self, nbPlayer) :
		# 1 for Player 1
		# 2 for Player 2
		if nbPlayer == 1 :
			for elem in self.getPlayer1().getTeam().getListChar() :
				if not elem.isDead() :
					return False
			return True
		elif nbPlayer == 2 :
			for elem in self.getPlayer2().getTeam().getListChar() :
				if not elem.isDead() :
					return False
			return True
		else :
			raise Exception("nbPlayer isn't 1 or 2")

	def isGameOver(self) :
		return self.testPlayerLoose(1) or self.testPlayerLoose(2)

	def testEquality(self) :
		return self.testPlayerLoose(1) and self.testPlayerLoose(2)

	def sendPlayer(self, nb, mess) :
		if nb == 1 :
			self.getPlayer1().getReferenceSocket().send(cb.listToStringBinary(mess))
		elif nb == 2 :
			self.getPlayer2().getReferenceSocket().send(cb.listToStringBinary(mess))
		elif nb == 3 :
			self.getPlayer1().getReferenceSocket().send(cb.listToStringBinary(mess))
			self.getPlayer2().getReferenceSocket().send(cb.listToStringBinary(mess))
		else :
			raise Exception("nb isn't 1 or 2 or 3")

	def recvPlayer(self, nb) :
		if nb == 1 :
			mess = self.getPlayer1().getReferenceSocket().recv(2048)
		elif nb == 2 :
			mess = self.getPlayer2().getReferenceSocket().recv(2048)
		elif nb == 3 :
			mess = self.getPlayer1().getReferenceSocket().recv(2048)
			mess = self.getPlayer2().getReferenceSocket().recv(2048)
		else :
			raise Exception("nb isn't 1 or 2 or 3")
		return cb.stringBinaryToList(mess)

	def run(self) :
		self.sendPlayer(1, [1, 1])
		self.sendPlayer(2, [1, 2])
		#Envois de l'arriver dans la room

		textEncode = decodeTeamInit(self.getPlayer1(), self.getPlayer2())
		if textEncode[0] == 666 :
			raise Exception("An Error Occured for the Creation of teams")
		self.sendPlayer(1, textEncode[0]) #On reçois d'abord son équipe puis celle de l'adv
		self.sendPlayer(1, textEncode[1])
		self.sendPlayer(2, textEncode[1])
		self.sendPlayer(2, textEncode[0])
		#Envois des équipes

		self.getMap().generationRelief()
		textEncode = encodeMap(self.getMap())
		if textEncode[0] == 666 :
			raise Exception("An Error Occured for the Creation of the Map")
		self.sendPlayer(3, textEncode)
		#envois de la Map

		turn = 1
		playerRunAway = False
		while not self.isGameOver() and not playerRunAway :
			isTurnOver = False
			while not isTurnOver :
				isTurnOver = False
				mess = self.recvPlayer(1) if turn % 2 == 1 else self.recvPlayer(2)
				textEncode, isTurnOver, playerRunAway = decodeMessFight(mess, self.getMap(), self.getPlayer1(), self.getPlayer2())
				if textEncode[0] == 666 :
					raise Exception("An Error Occured In The Fight.")
				self.sendPlayer(3, textEncode)
			turn += 1

		if not hasAskForQuit(mess, turn - 1, 1) :
			newthread = ClientThread(self.getPlayer1().getIP(), self.getPlayer1().getPort(), self.getPlayer1().getReferenceSocket(), self.getWaitingList())
			newthread.start()
		else :
			self.sendPlayer(1, [0])
			self.getPlayer1().getReferenceSocket().close()
			print("Client déconnecté :" + str(self.getPlayer1().getIP())+ " " + str(self.getPlayer1().getPort()))
		if not hasAskForQuit(mess, turn - 1, 2) :
			newthread2 = ClientThread(self.getPlayer2().getIP(), self.getPlayer2().getPort(), self.getPlayer2().getReferenceSocket(), self.getWaitingList())
			newthread2.start()
		else :
			self.sendPlayer(2, [0])
			self.getPlayer2().getReferenceSocket().close()
			print("Client déconnecté :" + str(self.getPlayer2().getIP())+ " " + str(self.getPlayer2().getPort()))

























class ThreadForPlayer(threading.Thread) :

	def __init__(self, P, tabPlayer, WaitingList, room) :
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
		self._room = room

	def getTabPlayer(self) :
		return self._tabPlayer

	def getPlayer(self) :
		return self._Player

	def getWaitingList(self) :
		return self._waitingList

	def getRoom(self) :
		return self._room

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
						#player.getReferenceSocket().send("Oh, votre adversaire est parti ! ...".encode())
						pass
			else :
				for player in self.getTabPlayer() :
					player.getReferenceSocket().send(r)