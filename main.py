#/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pygame
import settings

### Caption ###
pygame.display.init()
pygame.display.set_caption("Bobots - OcaStudios")

### Splash ###
folder = os.path.join('data','images', 'splash')
splash =[pygame.image.load(os.path.join(folder,i)).convert(32) for i in sorted(os.listdir(os.path.join(folder)))]
splash_size = splash[0].get_size()
os.environ['SDL_VIDEO_CENTERED'] = '1'
splash_surface = pygame.display.set_mode(splash_size, pygame.NOFRAME)
pygame.display.set_icon(pygame.image.load(os.path.join('data', 'images', 'favicon.png')).convert_alpha())
clock = pygame.time.Clock()
for i in splash:
	splash_surface.blit(i,(0,0))
	pygame.display.flip()
	pygame.time.wait(2000)#time to wait/ remove if it is a movie
	clock.tick(40)

pygame.mixer.init()
pygame.mixer.set_reserved(3)
pygame.init()


import g
import control
import scenes.menu
import game

if __name__=="__main__":
	g.scene = scenes.menu.Menu()
	while True:
		control.loop()
		game.loop()
		pygame.display.flip()
