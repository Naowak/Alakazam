import sys
sys.path.append("./map")
sys.path.append("./character")
sys.path.append("./tools")

from Character import *
from Map import *

from Road import *
from Sight import *

m = Map(30,30)
r = Road(30,30)
s = Sight(30,30)
c = Character("toto", 100, 60, 5)
c2 = Character("Pedro", 100, 60, 5)

def attaque15(loc1, loc2) :
	m.getCellCharacter(loc2).addLifePoint(-15)

loc1 = Location(2,2)
loc2 = Location(5,5)
c.setCharacterOnMap(loc1, m)
c2.setCharacterOnMap(loc2, m)
m.setCellType(Location(2,10), "Full")
m.setCellType(Location(12,20), "Full")

r.findRoadsForCells(c.getMouvementPoint(), c.getLocation(), m)
l = r.getListeCellsLocationWithRoads()
#for elem in l :
	#print(elem)

#print(c.getLocation())
s.fieldOfView(c.getLocation(), m)
print(s.string(c.getLocation(), m))

cap1 = Capacity("attaque15", attaque15, 0, 15, 0, True)

c.addCapacity(cap1)
m.getCellCharacter(loc1).useCapacity("attaque15", loc1, loc2, m)
#print(m)
#print(c)
#print(c2)

def effect2(char1, char2) :
	char2.addLifePoint(-3)

def effect6(char1, char2) :
	char2.addMana(-4)

e = Effect("2damage", effect2, [2,3,4,5], c2, c)
e2 = Effect("4mana", effect6, [3,5,6], c2, c)

#le = ListEffect()
#le.addEffect(e)
#le.addEffect(e2)

c.addEffectBeginTurn(e)
c.addEffectBeginTurn(e2)

for i in range(8) :
	c.applyEffectBeginTurn(i)
	print("TURN =========> " + str(i))
	print(c)
	print(c2)
	print('\n')

for elem in c._listEffectBeginTurn._list :
	print(elem)


