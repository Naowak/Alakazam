from Character import *
from Capacity import *
import sys
sys.path.append("../map")
from MapClient import *

def attaque5(loc1, loc2, M) :
	if M.getCell(loc2).getCharacter() :
		M.getCell(loc2).getCharacter().addLifePoint(-5)

c1 = Capacity("Ping", attaque5, 5, 10, 1, False)

class Archons(Character) :

	def __init__(self) :
		Character.__init__(self, "Archons", 100, 60, 5)
		self.addCapacity(c1)
