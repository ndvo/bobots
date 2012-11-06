import g

class Weapon():
	def __init__(self, level):
		self.fuel = None
		self.easy = []
		self.hard = []
		self.simplicity = 0
		self.level = level

	def power(self):
		return self.level

	def resource_cost(self):
		return self.level

	def extra_effect(self):
		pass

class DieselWeapon(Weapon):
	def __init__(self, level):
		Weapon.__init__(self,level)
		self.fuel = 'Diesel'
		self.easy = ['Insect', 'Rodent']
		self.hard = ['Bird']


class Firethrower(DieselWeapon):
	def __init__(self, level):
		DieselWeapon.__init__(self, level)
		self.simplicity = -10

	def power(self): return 20+(10*self.level)

	def resource_cost(self): return 2+(2*self.level)


class Fireball(DieselWeapon):
	def __init__(self,level):
		DieselWeapon.__init__(self,level)
		self.simplicity = 50

	def power(self): return 10*self.level

	def resource_cost(self): return 1+self.level

class Napalm(DieselWeapon):
	def __init__(self,level):
		DieselWeapon.__init__(self,level)
		self.simplicity = -10
	
	def power(self): return 5*self.level*turn#Ainda nao esta claro como pegar o turno 

	def extra_effects(self):
		if self.im_self == g.PC:
			victim = g.Foe
		else:
			victim = g.PC
		try:
			if victim.burning_turns < self.level:
				victim.burning_turns += 1
			else:
				del victim.burning_turns	
		except NameError:
			victim.burning_turns = 1

class Bomb(DieselWeapon):
	def __init__(self,level):

