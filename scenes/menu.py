import g
import os
import pygame
import widgets
import interface
import actions
import scenes


class Menu(scenes.Scene):
	place = widgets.Place(os.path.join('extras','initial_screen'))
	message = 'Welcome'
	place =  widgets.Place(os.path.join('extras','initial_screen'))

	def __init__(self):
		g.board = widgets.MessageBoard()
		scenes.Scene.__init__(self, )
		self.menu = self.menu_main()

	def menu_main(self):
		return [widgets.Button(i[0],i[1],(5, g.button_slots[i[2]]),i[3],back=i[4]) for i in (
			['Start new game',"The adventure is about to begin", 0, self.new_game,'01'],
			['Load saved game', "Whatch out everyone, I'm back!", 1, self.menu_load_game,'02'],
			['Change preferences', "I'll have it my own way.", 2, self.menu_settings,'03'],
			['See credicts', "Who's fault is this?", 3, self.start_game,'04']
		)]	

	def menu_settings(self):
		g.menu = [widgets.Button(i[0],i[1],(5, g.button_slots[i[2]]),i[3], back = i[4]) for i in (
			['Resolution','Strach or squash to fit', 0, self.menu_main, '01'],
			['Volume',"Could you speak louder, please?", 1, self.menu_main,'02'],
			['Controls',"Let's shuffle some keys", 2, self.menu_main,'03'],
			['Language',"Ask Babel Fish some help", 3, self.menu_main,'04']
		)]

	def menu_load_game(self):
		savefiles = [i for i in  os.listdir('saves') if i[-7:]=='.bobots' ][0:4]
		g.menu = []
		counter = 0
		for i in savefiles:
			filepath = os.path.join(os.getcwd(),'saves',i)
			S = save.Saved_Game(filepath)
			g.menu.append(
				widgets.Button(
					"%s, level %s" % (
						S.robot1['type'],
						S.robot1['level']
						),
					"Money: $%s Rank: %s" % (
							S.money,
							S.rank
						),
					(5,g.button_slots[counter]),
					self.load_game, counter,
					arguments = {'filepath': filepath}
					)
				)
			counter += 1
	
	def start_game(self):
		g.menu = []
	
	def load_game(self, **kwargs):
		S = save.Saved_Game(kwargs['filepath'])
		g.PC = widgets.Char(S.char.lower(), rank=S.rank, place=S.place, side='left', milestones=S.milestones, money = S.money)
		g.foe = widgets.Char('scientist', side='right')
		g.foe.lines['center'] = "You could never guess what I have for you today."
		g.game_status = 'game'
		g.scene = scenes.squirrelton.House()
		g.PC.action = g.PC.arrive
		g.foe.action = g.foe.arrive
		g.board.new_message("Let's start a new game")
		g.pending_actions.append(interface.transition)
		
	def new_game(self):
		g.next_scene = scenes.squirrelton.House()
		g.PC = widgets.Char('nerd', side='left')
		g.foe = widgets.Char('scientist', side='right')
		g.foe.lines['center'] = "You could never guess what I have for you today."
		g.PC.action = g.PC.arrive
		g.foe.action = g.foe.arrive
		g.board.new_message("Let's start a new game")
		g.pending_actions.append(interface.transition)

