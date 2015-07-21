import sys
sys.path.append("../map")
from Map import *
sys.path.append("../character")
from Character import *
from Effect import *

class TimeEffect(Effect):
	"""Type particulier d'effet :
	effet active a chaque tour pendant un nombre de tours donne"""
	
	def debuff(self):
		self.getListTurn().pop(-1)