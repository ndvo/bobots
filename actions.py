import g
import interface
import widgets

class Battle():
	def __init__(self):
		print "Battle started"
		self.sequence = [g.PC, g.foe] #TODO call function that calculates the first strike
		self.battle_round = 1
		self.turn = 0
		self.acting = self.sequence[self.turn]
		"""Creates a menu for the player to choose his bobot"""
		g.scene.menu = [widgets.Button(bobot.gender, bobot.color+" "+bobot.stage, (5, g.button_slots[g.PC.robots.index(bobot)]), bobot.choose_me) for bobot in g.PC.robots ]
		g.pending_actions.append(interface.fight)
		g.pending_actions.append(self.start_battle)
		#TODO fix the selection of foe bobot, for now it takes the first one

	def build_menu(self):
		g.scene.menu = [
			widgets.Button(i[0],i[1],(5,g.button_slots[i[2]]),i[3],back=i[4]) for i in(
				[ 'Attack', "It's time to suffer", 0, self.attack, '01' ],
				[ 'Wait', "Hum... Let me think", 1, self.wait, '02']
			)
		]

	def start_battle(self):
		"""Start the battle using the chosen bobots  """
		done = False
		if interface.fight not in g.pending_actions and g.PC.chosen_bobot:
			self.build_menu()
			done = True
		return done

	def next_turn(self):
		self.acting = self.sequence[self.turn]
		if self.turn:
			self.battle_round += 1
		self.turn = not self.turn
		self.build_menu()
		return True

	def wait(self):
		g.pending_actions.append(self.next_turn)

	def attack(self):
		attacker = self.sequence[self.turn]
		attacker.chosen_bobot.action_attack()
		g.pending_actions.append(self.got_hit)
		g.pending_actions.append(self.end_attack)

	def got_hit(self):
		done = False
		attacker = self.sequence[self.turn]
		target = self.sequence[not self.turn]
		if attacker.chosen_bobot.sprite.step_no > attacker.chosen_bobot.sprite.total_steps/2:
			target.chosen_bobot.action_get_hit()
			done = True
		return done

	def end_attack(self):
		done = False
		attacker = self.sequence[self.turn]
		target = self.sequence[not self.turn]
		if attacker.chosen_bobot.sprite == attacker.chosen_bobot.attack \
		and attacker.chosen_bobot.sprite.step_no == attacker.chosen_bobot.sprite.total_steps-1:
			g.pending_actions.append(self.next_turn)
			done = True
		return done

class CategoryAttack():
	def __init__(self):
		self.strenght = []
		self.weakness = []



class Attack():
	def __init__(self, category, power):
		self.category = category
		self.power = power


