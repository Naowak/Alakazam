import ManageBattle as mb
import sys
sys.path.append("../map/")
from Location import *
sys.path.append("../character")
import Archons

def decodeTeamInit(player1, player2) :
	code1 = [1, 1] + player1.getTeam()
	code2 = [1, 1] + player2.getTeam()
	for player in [player1, player2] :
		if player.getTeam()[0] == 1 :
			c1 = "NormalClass"
		try :
			mb.createTeamInit([c1, c1, c1], player)
		except :
			print("An error Occured")
			return [666]
	return [code1, code2]

def encodeMap(m) :
	l = list()
	l += [2]
	l += [m.getTailleX()]
	l += [m.getTailleY()] 
	for i in range(m.getTailleX()) :
		for j in range(m.getTailleY()) :
			l += [m.getCell(Location(i, j)).getType()]
	return l

def decodeMessFight(mess, m, p1, p2) :
	if len(mess) == 2 and mess[0] == 0 and mess[1] == 1 :
		#Joueur abandonne la partie
		return [0, 1], True, True
	elif len(mess) == 1 and mess[0] == 0 :
		#Joueur quitte le jeu
		return [0, 1], True, True
	elif len(mess) == 1 and mess[0] == 3 :
		#Changement de tour
		return [3], True, False
		#On envois seulement que le tour change, les clients doivent alors gérer d'eux même pour savoir si c'est à eux de jouer ou non
	elif len(mess) > 1 and mess[0] == 100 :
		#Mouvement d'un personnage
		if len(mess) % 2 == 0 :
			raise Exception("nombre pair de case dans le tableau")
		mb.moveCharacter(mess[1:], m)
		return mess, False, False






