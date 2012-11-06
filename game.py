# -*- coding: utf-8 -*-

import pygame
import os
import g
import widgets
import scenes.squirrelton
import settings

def loop():
	"""
	This is the game's main loop and it does the following:
	- runs every function in g.pending_actions list and remove it from the list if it returns anything.
	- blit the background of menu and main frame
	- run the on_loop function and blit the image or animation of every item in g.scene.menu
	- run the on_loop function and blit the image or animation of every item in main (main is hardcoded)
	- run functions on the following events:
		- chars begin entrance
		- chars entering
		- chars on center
		- chars begin leaving
		- chars leaving
	- blit messages on their positions
	- blit it all on the screen
	- blit the balloons on the screen

	Please, update the description on every change
	"""
	g.milliseconds += g.clock.tick()
	if g.milliseconds > settings.fps:
		g.milliseconds = 0

	#Runs the main loop
	#a pending action only returns true if it should no longer be executed
	for i in g.pending_actions:
		done = i()
		if done:
			g.pending_actions.remove(i)
	#reset the frames
	g.text_frame.blit(g.text_background, (0,0))
	g.menu_frame.blit(g.menu_background, (0,0))
		
	#run the menu items
	for i in g.scene.menu:
		i.on_loop()
		if i.__class__ == widgets.Button:
			g.menu_frame.blit(i.background, i.pos,(i.area[i.status],(264,66)))
		g.menu_frame.blit(i.image,i.pos)
	#run items in main frame
	for i in (g.next_scene, g.scene):
		if i and i.place:
			i.place.on_loop()
			g.main_frame.blit(i.place.animation, i.place.pos, ((i.place.step,0), i.place.size))
	for i in (g.PC, g.foe):
		if i:
			i.on_loop()
			g.main_frame.blit(i.animation, i.pos,((i.step,0),i.size))
	for i in (g.PC, g.foe):
		if i and i.chosen_bobot:
			i.chosen_bobot.on_loop()
			g.main_frame.blit(i.chosen_bobot.animation, i.chosen_bobot.pos,((i.chosen_bobot.step,0), i.chosen_bobot.size))
	if g.panel:
		panel=g.panel
		panel.on_loop()
		g.main_frame.blit(panel.image, panel.pos)

	if g.PC:
		g.menu_frame.blit(g.PC.status, (10,10))
		if g.PC.pos[0]<=-100 and g.PC.side == 'left':
			g.scene.on_start_enter()
		elif g.PC.pos[0] > -100 and g.PC.animation == g.PC.walk:
			g.scene.on_entering()
		elif g.on_center:
			g.scene.on_center()
		elif g.PC.pos[0] < 180 and g.PC.animation == g.PC.walk:
			g.scene.on_start_leave()

	for (p,i) in zip(g.slots, [i for sub in g.board.messages for i in sub] ):
		g.text_frame.blit(i,(35,p))
	
	g.screen.blit(g.main_frame,g.main_pos)
	g.screen.blit(g.text_frame,g.text_pos)
	g.screen.blit(g.menu_frame,g.menu_pos)
	if g.board.side == 'none':
		board_pos = (20,355)
	else:
		board_pos = (20,265)
	g.screen.blit(g.board.balloons[g.board.side], board_pos)
	for i in g.board.headline:
		g.screen.blit(i, (30, 360)) 

def teste():
	pass

def speak_on_center(char, line):
	if (180 > char.pos[0] > 169 and char.side == 'left') \
	or (320 > self.pos[0] > 301 and self.side == 'right'):
		g.board.new_message(line)

	
