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
		self._yourTurn = False

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

	def yourTurn(self) :
		return self._yourTurn

	def setYourTurn(self, boolean) :
		self._yourTurn = boolean



def decodeTeamInit(mess) :
	if mess[0] == 1 :
		return Team(Archons.Archons(), Archons.Archons(), Archons.Archons())
	else :
		print("pas de team pour toi ? :")
		print(mess[0])

def moveCharacter(TR, mess) :
	char = TR.getBattle().getMap().getCellCharacter(Location(mess[0], mess[1]))
	i = 0
	while i < (len(mess) // 2) - 1 :
		#affichage
		pass
	TR.getBattle().getMap().setCellCharacter(l, char)
	TR.getBattle().getMap().setNoCharacter(Location(mess[0], mess[1]))


def decodeMessClient(TR, mess) :

	if len(mess) == 1 and mess[0] == 0  :
		#Ordre de déconnecter
		TR.setContinue(False)
		TR.getThreadSending().setContinue(False)
		print("Deconnexion...")

	if len(mess) == 2 and mess[0] == 0 and mess[1] == 1 and TR.getBattle() :
		#Ordre de finir la Battle 
		TR.deleteBattle()
		TR.getBattle().setYourTurn(False)

	elif len(mess) == 2 and mess[0] == 1 and  not TR.getBattle() :
		#Ordre d'initialiser une Battle
		b = Battle()
		TR.setBattle(b)
		TR.getThreadSending().setBattle(b)
		TR.getBattle().setNbPlayer(mess[1])

	elif len(mess) > 2 and mess[0] == 1 and mess[1] == 1 and TR.getBattle() :
		#Ordre de créer les deux teams pour les deux joueurs (l'un après l'autre)
		if not TR.getBattle().getPlayer1().getTeam() :
			#si joueur1 n'a aucune team : à lui (par défault j1 = toi)
			TR.getBattle().getPlayer1().setTeam(decodeTeamInit(mess[2:]))
			print(TR.getBattle().getPlayer1().getTeam())
		elif not TR.getBattle().getPlayer2().getTeam() :
			#si j2 n'a aucune team (donc j1 aussi), à j2. j2 = adversaire
			TR.getBattle().getPlayer2().setTeam(decodeTeamInit(mess[2:]))
			print(TR.getBattle().getPlayer2().getTeam())
		else :
			#les deux joueurs ont déjà une team, on ne peut pas en rajouter...
			raise Exception("Both player have already a Team")

	elif len(mess) > 1 and mess[0] == 2 and TR.getBattle() :
		#Ordre de créer la Map
		TR.getBattle().setMap(MapClient(mess[1:]))
		print(TR.getBattle().getMap())

	elif len(mess) == 1 and mess[0] == 3 and TR.getBattle() :
		#Ordre de changer de tour
		TR.getBattle().setYourTurn(not TR.getBattle().yourTurn())
		print("Hey, Change of turn !")

	elif len(mess) > 5 and len(mess) % 2 == 1 and  mess[0] == 100 and TR.getBattle() :
		moveCharacter(TR, mess[1:])


	else :
		#rien ne va
		print("La pas bon" + str(mess))

