# -*- coding: utf-8 -*-


import pygame
import os

blitlist = {
	'main':[],
	'menu':[],
	'text':[],
}

#Screen contents
status = []

#Layout elements
screen = pygame.display.set_mode((800,500))
main_frame = pygame.Surface((570, 350))
menu_frame = pygame.Surface((230, 500))
text_frame = pygame.Surface((570, 150)) 
main_pos = (0,0)
text_pos = (0,350)
menu_pos = (570,0)


#Directories
dir_main = os.getcwd()
dir_data = os.path.join(dir_main,'data')
dir_images = os.path.join(dir_main,'data','images')
dir_scenario = os.path.join(dir_main,'data','images','scenario')
dir_char = os.path.join(dir_main,'data','images','chars')
dir_interfaces = os.path.join(dir_main,'data','images','interface')
dir_windows = os.path.join(dir_main, 'data','images','windows')
dir_buttons = os.path.join(dir_main,'data','images','buttons')


#Background elements
menu_background = pygame.image.load(os.path.join(dir_windows,'left-buttons.png')).convert()
text_background = pygame.image.load(os.path.join(dir_windows,'lower-text.png')).convert()

#Fonts
fontbold = pygame.font.Font(os.path.join('data','fonts','Ubuntu-B.ttf'), 18)
fonthuge = pygame.font.Font(os.path.join('data','fonts','Ubuntu-R.ttf'), 60)
font = pygame.font.Font(os.path.join('data','fonts','Ubuntu-R.ttf'), 14)
fontmessage = pygame.font.Font(os.path.join('data','fonts', 'Ubuntu-R.ttf'), 16)
fontmessagebold = pygame.font.Font(os.path.join('data','fonts', 'Ubuntu-B.ttf'),16)

#messages
board = None
slots = [40, 60, 80, 100, 120]
button_slots = [60, 140, 220, 300, 380, 420, 500]

#Interactive elements
scene = None
next_scene = None
PC = None
Robot = None
foe = None
on_center = False
game_status = 'menu' #It can be menu, game or pause
mouse_pos = pygame.mouse.get_pos()
mouse_button_up = 0
mouse_button_down = [0,0]#buttonnumber, time holding 
pending_actions = []
panel = None

#Useful stuff
sides = {'right': {'name':'right', 'number':1,'opposite':'left'},
	'left': {'name': 'left', 'number':-1,'opposite':'right'}}
clock = pygame.time.Clock()
milliseconds = 0 
