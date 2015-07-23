import socket
import threading
from Player import *

class Battle(threading.Thread) :

	def __init__(self, player1, player2) :
		threading.Thread.__init__(self)
		if not isinstance(player1, Player) :
			raise Exception("player1 isn't a Player")
		if not isinstance(player2, Player) :
			raise Exception("player2 isn't a Player")

		self._player1 = player1
		self._player2 = player2

	def getPlayer1(self) :
		return self._player1

	def getPlayer2(self) :
		return self._player2

	def run(self) :
		self.getPlayer1().getReferenceSocket().send("Bienvenue.".encode())
		self.getPlayer2().getReferenceSocket().send("Casse toi. Wesh. Cordialement.".encode())
		while(1) :
			r1 = self.getPlayer1().getReferenceSocket().recv(2048)
			r2 = self.getPlayer2().getReferenceSocket().recv(2048)
			self.getPlayer2().getReferenceSocket().send(r1)
			self.getPlayer1().getReferenceSocket().send(r2)

