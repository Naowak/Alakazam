from Team import *
from Map import *


def createTeamInit(l, player) :
	li = []
	for elem in l :
		if elem == "NormalClass" :
			li += [Character("Normal", 100, 60, 5)]
	player.setTeam(Team(li[0],li[1],li[2]))

def moveCharacter(mess, m) :
	i = 1
	k = Location(mess[0], mess[1])
	while(i < len(mess)//2 ) :
		l = Location(mess[2*i], mess[2*i+1])
		test = False
		for elem in m.getCellListeVoisins(k) :
			if l.equals(elem) :
				test = True
		if not test :
			raise Exception("l n'est pas dans la liste des voisins de k")
		if m.isCellType(l, "Full") or m.isCellType(l, "Taken") :
			raise Exception("l est soit Full soit Taken")
		k = l
		i += 1
	m.setCellCharacter(l, m.getCellCharacter(Location(mess[0], mess[1])))


		

