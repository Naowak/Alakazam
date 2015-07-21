import sys
sys.path.append("../map")
from Map import *
sys.path.append("../character")
from Character import *
from Effect import *

class Buff(Effect):
	
	"""Les Buffs sont des effets particuliers : 
	Bonus/malus recu au lancement du sort pour un nombre de tours limite"""
	
	def debuff(self):
		for k in range(len(self.getListTurn())):
			self.getListTurn()[k]+= -1
