import sys
sys.path.append("../tools/")
import convertBinary as cb
sys.path.append("../character/")
from Team import *
import Archons

def decodeTeamInit(mess) :
	if mess[0] == 1 :
		return Team(Archons.Archons(), Archons.Archons(), Archons.Archons())
	else :
		print("pas de team pour toi ? :")
		print(mess[0])

