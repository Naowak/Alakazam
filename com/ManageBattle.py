from Team import *

def createTeamInit(l, player) :
	li = []
	for elem in l :
		if elem == "NormalClass" :
			li += [Character("Normal", 100, 60, 5)]
	player.setTeam(Team(li[0],li[1],li[2]))