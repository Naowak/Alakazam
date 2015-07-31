from ManageBattle import *
import sys
sys.path.append("../map/")
from Location import *

def decodeTeamInit(player1, player2) :
	code1 = player1.getTeam()
	code2 = player2.getTeam()
	for player in [player1, player2] :
		if player.getTeam()[0] == 1 :
			c1 = "NormalClass"
		try :
			createTeamInit([c1, c1, c1], player)
		except :
			print("An error Occured")
			return [666]
	return [code1, code2]

def encodeMap(m) :
	l = list()
	l += [m.getTailleX()]
	l += [m.getTailleY()] 
	for i in range(m.getTailleX()) :
		for j in range(m.getTailleY()) :
			l += [m.getCell(Location(i, j)).getType()]
	return l


