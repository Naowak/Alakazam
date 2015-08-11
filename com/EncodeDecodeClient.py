import sys
sys.path.append("../tools/")
import convertBinary as cb
sys.path.append("../character/")
from Team import *
from PlayerClient import *
from MapClient import *
import Archons

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
		return self._player2

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



def decodeTeamInit(mess) :
	if mess[0] == 1 :
		return Team(Archons.Archons(), Archons.Archons(), Archons.Archons())
	else :
		print("pas de team pour toi ? :")
		print(mess[0])

def decodeMessClient(threadReception, mess) :

	if(len(mess) == 1 and mess[0] == 0) :
		#Ordre de déconnecter
		threadReception.setContinue(False)
		threadReception.getThreadSendind().setContinue(False)
		print("Deconnexion...")

	elif(len(mess) == 2 and mess[0] == 1) :
		#Ordre d'initialiser une Battle
		b = Battle()
		threadReception.setBattle(b)
		threadReception.getThreadSendind().setBattle(b)
		threadReception.getBattle().setNbPlayer(mess[1])

	elif(len(mess) > 2 and mess[0] == 1 and mess[1] == 1) :
		#Ordre de créer les deux teams pour les deux joueurs (l'un après l'autre)
		if not threadReception.getBattle().getPlayer1().getTeam() :
			#si joueur1 n'a aucune team : à lui (par défault j1 = toi)
			threadReception.getBattle().getPlayer1().setTeam(decodeTeamInit(mess[2:]))
			print(threadReception.getBattle().getPlayer1().getTeam())
		elif not threadReception.getBattle().getPlayer2().getTeam() :
			#si j2 n'a aucune team (donc j1 aussi), à j2. j2 = adversaire
			threadReception.getBattle().getPlayer2().setTeam(decodeTeamInit(mess[2:]))
			print(threadReception.getBattle().getPlayer2().getTeam())
		else :
			#les deux joueurs ont déjà une team, on ne peut pas en rajouter...
			raise Exception("Both player have already a Team")

	elif(len(mess) > 1 and mess[0] == 2) :
		threadReception.getBattle().setMap(MapClient(mess[1:]))
		print(threadReception.getBattle().getMap())

	else :
		#rien ne va
		print("La pas bon" + str(mess))

