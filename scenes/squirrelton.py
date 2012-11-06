import g
import os
import pygame
import widgets
import interface
import actions
import scenes

def button_street():
	g.board.new_message("Enough of home, I'm now looking for trouble.")
	g.PC.action = g.PC.go_on
	g.foe.action =g.foe.go_on
	g.pending_actions.append(interface.transition)
	g.next_scene = Street()
  

class House(scenes.Scene):
	place = widgets.Place(os.path.join('squirrelton','house'))
	count = 0
	wait = False
	dialog_key = False
	speech = 0

	def ready(self):
		self.dialogs = {
		 1 : ("Take this bobot, son, and become the greates champion!",(
				('Take the bobot', "Wow! That's great dad.",0, button_street,'01'),
				('Give it up', "I need no bobot!!",1, self.change,'02')
			)),
		 2 : ("You could never guess what I have for you today",(
				('What?', "C'moooon, tell me yet!", 0, self.change,'01'),
				("I bet it is boring", "I'm lousy on guessing.",1, self.change,'02'),
			))}
		self.speeches = ("I have to talk to you", 
			"When I was about your age my father called me...",
			""""You're old enough", he said, it's time to know what's important.""", 
			"and now it is your turn", 
			)
		#scenes.Scene.__init__(self)

	def on_center(self):
		if self.speech == 0:
			self.next()
			
		if self.dialog_key:
			if self.wait and self.wait < 1000:
				self.wait -= 1
			if not self.wait:
				g.board.new_message(self.dialogs[self.dialog_key][0], side = "right")
				self.menu = [widgets.Button(i[0],i[1],(5,g.button_slots[i[2]]),i[3],back=i[4]) for i in self.dialogs[self.dialog_key][1]]
				print self.menu
				self.wait = 1001

	def next(self):
		if self.speech < len(self.speeches):
			g.board.new_message(self.speeches[self.speech], side = "right")
			self.menu = [widgets.Button(i[0],i[1],(5,g.button_slots[i[2]]),i[3],back=i[4]) for i in (
				['Next', 'Proceed, please.', 0, self.next, '01'],
			)]
			self.speech += 1
		else:
			self.dialog_key = 1

	def change(self):
		g.board.new_message("Answer from the player", side="left")
		g.menu = []
		self.wait = 40
		if self.dialog_key == 1:
			self.dialog_key = 2
		else:
			self.dialog_key = 1	


class Street(scenes.Scene):
	place =  widgets.Place(os.path.join('squirrelton','street'))
	foe = widgets.Char('bully',side='right')
	count = 0
	battle = None

	def on_start_enter(self):
		self.count = 0
		g.foe = self.foe
		g.foe.action = g.foe.arrive
		g.foe.lines['center'] = "What do you think you are doing in MY street?"
		g.foe.robots.append(widgets.Robot(g.foe, 'rodent', 'two', 'natural'))

	def on_center(self):
		if not self.count:
			g.board.new_message("So you have a bobot! Let's fight!", side = "right")
			self.menu = [widgets.Button(i[0],i[1],(5,g.button_slots[i[2]]),i[3],back=i[4]) for i in(
				['Challenge',"You are no match for any prototype I've designed", 0, self.button_challenge, '01'],
				['Run Away', "So sorry, sir, I didn't mean to disturb", 1, self.button_runaway,'02'],
				['To the park',"I need some fresh air", 2, self.button_park, '03'],
				['To the school',"Maybe I should try to learn something", 3, self.button_school,'04']
			)]
		self.count +=1
	
	def button_challenge(self):
		self.battle = actions.Battle()
		g.pending_actions.append(interface.fight)
		self.battle.choose_your_bobots()
		g.menu = []

	def button_runaway(self):
		pass

	def button_park(self):
		if not self.count:
			g.board.new_message("I'll go to the park and see some birds.")
			g.PC.action = g.PC.go_on
			g.foe.action =g.foe.go_on
			g.pending_actions.append(interface.transition)
			g.scenes = Park()
			self.count +=1

	def button_school(self):
		pass


class Park(scenes.Scene):
	foe =  widgets.Char('bully',side='right')
	place = widgets.Place(os.path.join('squirrelton','park'))
	count = 0

	def __init__(self):
		self.menu = [widgets.Button(i[0],i[1],(5,i[2]),i[3],back=i[4]) for i in(
					['Challenge',"You are no match for any prototype I've designed", 60, self.button_challenge, '01'],
					['Run Away', "So sorry, sir, I didn't mean to disturb", 160, self.button_runaway,'02'],
					['To the street',"I need some fresh air", 260, self.button_street, '03'],
					['To the school',"Maybe I should try to learn something", 360, self.button_school,'04']
			)]

	
		scenes.Scene.__init__(self,)

	def on_center(self):
		pass

	def button_challenge(self):
		print 'challenging'

	def button_runaway(self):
		pass

	def button_school(self):
		pass
