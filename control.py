import pygame
import g
from pygame.locals import *
from sys import exit


def loop():
	g.mouse_pos = pygame.mouse.get_pos()
	for event in pygame.event.get():
		g.mouse_button_up = 0
		if event.type == QUIT:
			exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				exit()
		elif event.type == MOUSEBUTTONUP:
			g.mouse_button_up = event.button
		if event.type == MOUSEBUTTONDOWN:
			if g.mouse_button_down[0] == event.button:
				g.mouse_button_down[1]+=1
			else:
				g.mouse_button_down[1]=0
			g.mouse_button_down[0] = event.button
		else:
			g.mouse_button_down = [0,0] 

	pygame.event.clear()

