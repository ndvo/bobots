import g
import widgets

class Battle():
	def __init__(self):
		self.sequence = [g.PC, g.foe] #TODO call function that calculates the first strike
		self.battle_round = 1
		self.turn = 0
		self.acting = self.sequence[self.turn]

	def choose_your_bobots(self):
		"""Creates a menu for the player to choose his bobot"""
		g.next_menu = [ widgets.Button(bobot.gender, bobot.color+" "+bobot.stage, (5, g.button_slots[g.PC.robots.index(bobot)]), bobot.choose_me) for bobot in g.PC.robots ]
		g.pending_actions.append(self.start_battle)
		#TODO fix the selection of foe bobot, for now it takes the first one
		if not g.foe.chosen_bobot:
			g.foe.chosen_bobot = g.foe.robots[0]

	def start_battle(self):
		"""Start the battle using the chosen bobots  """
		done = False
		if g.PC.chosen_bobot:
			g.menu = [
				widgets.Button(i[0],i[1],(5,g.button_slots[i[2]]),i[3],back=i[4]) for i in(
					[ 'Attack', "It's time to suffer", 0, self.attack, '01' ],
					[ 'Wait', "Hum... Let me think", 1, self.wait, '02']
				)
			]
			done = True
		return done

	def next_turn(self):
		self.acting = self.sequence[self.turn]
		if self.turn:
			self.battle_round += 1
		self.turn = not self.turn
		return True

	def wait(self):
		g.pending_actions.append(self.next_turn)

	def attack(self):
		attacker = self.sequence[self.turn]
		attacker.chosen_bobot.step = 0
		attacker.chosen_bobot.animation = attacker.chosen_bobot.attack
		g.pending_actions.append(self.got_hit)
		g.pending_actions.append(self.end_attack)

	def got_hit(self):
		done = False
		attacker = self.sequence[self.turn]
		target = self.sequence[not self.turn]
		if attacker.chosen_bobot.step > len(attacker.chosen_bobot.attack)/2:
			target.chosen_bobot.step= 0
			target.chosen_bobot.animation = target.chosen_bobot.ouch
			done = True
		return done

	def end_attack(self):
		done = False
		attacker = self.sequence[self.turn]
		target = self.sequence[not self.turn]
		if attacker.chosen_bobot.animation == attacker.chosen_bobot.attack \
		and attacker.chosen_bobot.step == len(attacker.chosen_bobot.attack)-1:
			g.pending_actions.append(self.next_turn)
			done = True
		return done
