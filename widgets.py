import os
import pygame
import random
import settings
import g
import dicts

class Place():
	def __init__(self, name):
		self.folder = os.path.join(g.dir_scenario, name)
		self.pos = (0,0)
		self.step = 0
		self.animation = pygame.image.load(self.folder+'.png').convert_alpha()
		self.action = 'stay'
		self.size = (570,350)

	def leave(self):
		self.action = 'leave'
	
	def on_loop(self):
		if g.milliseconds == 0 \
		and self.action == 'leave' \
		and g.PC \
		and (g.PC.pos[0] < 104 or g.PC.pos[0] > 574):
			if self.step <= self.animation.get_width()-self.size[0]:
				self.step += self.size[0]
			else:
				self.action = 'out'


class Text():
	def __init__(self, text, pos, frame, color = (0,0,0), font = g.font):
		self.text = text
		self.pos = pos
		self.image = font.render(text, 1, color)
		self.frame = frame

	def on_loop(self):
		pass#self.frame.blit(self.image, self.pos)

class MessageBoard():
	def __init__(self):
		self.side = 'none'
		self.headlinetext = ''
		self.headline = []
		self.messages = []
		self.balloons = {
		'left':   pygame.image.load(os.path.join(g.dir_interfaces, 'balloon-left.png')).convert_alpha(), 
		'right':  pygame.image.load(os.path.join(g.dir_interfaces, 'balloon-right.png')).convert_alpha(), 
		'none':pygame.image.load(os.path.join(g.dir_interfaces, 'balloon-none.png')).convert_alpha(), 
		}
		
	def new_message(self, text, side='none'):
		self.side = side
		self.messages.insert(0, message(self.headlinetext, 500, g.fontmessage))
		self.headline = message(text, 500, g.fontmessagebold)
		self.headlinetext = text
		if len(self.messages) > 5:
			del self.messages[5]


def message(text, max_lenght, font):
	images = []
	text_list = text.split()
	number_of_words = len(text_list)
	count = 0
	height=0
	first = True
	line = ""
	line_break  = False
	color=(0,0,0,0)
	while count < number_of_words:
		line += text_list[count]
		line_size = font.size(line)
		if line_size[0] < max_lenght:
			if count+1 < number_of_words:
				temporary_line = line+' '+text_list[count+1]
				if font.size(temporary_line)[0] >= max_lenght:
					images.append(font.render(line,1, color))
					line = ""
				else:
					line += ' '
			elif count+1 == number_of_words:
				images.append(font.render(line, 1, color))
		else:
			line = text_list[count]
			height += int(line_size[1]*.8)
		count += 1
	return images



class Button():
	backgrounds = [pygame.image.load(os.path.join(g.dir_buttons,i)).convert_alpha() for i in os.listdir(os.path.join(g.dir_buttons)) if i[0:3] == 'btn']
	def __init__(self, title, text, pos, function,  back='01', arguments = {}):
		self.title = title
		self.text = text
		self.pos = pos
		self.image = pygame.Surface((220,66), pygame.SRCALPHA).convert_alpha()
		self.background = self.backgrounds[int(back)]
		self.image.blit(g.fontbold.render(title,1,(0,0,0)), (10,4))
		text_images = message(text, 200, g.font)
		for p,i in zip(((10,27),(10,43)), text_images ):
			self.image.blit(i,p)
		self.size = self.image.get_size()
		self.rect = pygame.Rect((pos[0]+g.menu_pos[0]+5,pos[1]+g.menu_pos[1]+0) , self.size)
		self.execute = function
		self.status = None
		self.area = {
			None:(0,0),
			'hover':(0,66),
			'active':(0,132),
			'locked':(0,198)
		}
		self.arguments = arguments

	def on_loop(self):
		if self.rect.collidepoint(g.mouse_pos):
			if self.status != "active":
				self.status = "hover"
			if g.mouse_button_down[0] == 1:
				self.status = 'active'
		else:
			self.status = None


		if g.mouse_button_up == 1:
			if self.rect.collidepoint(g.mouse_pos):
				if self.status == 'active':
					self.execute(**self.arguments)
					self.status = None

class Icon():
	def __init__(self, image,pos, function,frame='menu'):
		self.image = pygame.image.load(os.path.join(g.dir_icons,image)).convert_alpha()
		self.execute = function
		self.status = None
		self.frame = frame
		frame_pos = [
			(g.main_frame,g.main_pos),
			(g.menu_frame,g.menu_pos),
			(g.text_frame,g.text_pos)
		]
		for i in frame_pos:
			if i[0] == self.frame:
				self.frame_pos = i[1]
		self.pos = pos
		self.rect = pygame.Rect((self.frame_pos[0]+pos[0],self.frame_pos[1]+pos[1]), self.image.get_width)

	def on_loop(self):
		self.frame.blit(self.image,self.pos)
		if self.rect.collidepoint(g.mouse_pos) \
		and g.mouse_button_down[0] == 1:
			for i in g.menu:
				if i.status:
					i.status = None
			self.status = 'active'
		if self.status == 'active' \
		and self.rect.collidepoint(g.mouse_pos) \
		and g.mouse_button_up == 1:
			self.execute()

class Char():
	def __init__(self, name, rank=20, place='home',side='right', milestones = [], money=0):
		self.name = name
		self.rank = rank
		folder = dicts.characters[name]['folder']
		self.side = side
		self.milestones = []
		self.place = ''
		if self.side=='left':
			self.pos = [-110,190]
		else:
			self.pos = [580,190]
		attributes = ['celebrate','lose','offer','shaken','stay','walk','yes']
		for i in attributes:
			if self.side == 'right':
				self.__dict__[i] = pygame.transform.flip(pygame.image.load(os.path.join(g.dir_char, folder, i+'.png')).convert_alpha(), 1,0)
			else:
				self.__dict__[i] = pygame.image.load(os.path.join(g.dir_char, folder, i+'.png')).convert_alpha()
		self.animation = self.stay
		self.step = 0
		self.action = None
		self.robots = []
		self.chosen_bobot = None
		self.lines = {'defeat':None, 'victory':None,}
		self.size = 100,100
		self.money = money 
		self.status = self.update_status()
		
	def on_loop(self):
		if g.milliseconds ==0:
			if self.step < self.animation.get_width()-self.size[0]:
				self.step += self.size[0]
			else:
				self.step = 0
		if self.action:
			self.action()
		else:
			self.animation = self.stay

	def arrive(self):
		if self.animation != self.walk:
			self.step = 0
		if g.milliseconds == 0:
			self.animation = self.walk
			if (self.pos[0] < 169 and self.side == 'left') \
			or (self.pos[0] > 301 and self.side == 'right'):
				self.pos[0] -= 3*g.sides[self.side]['number']
			else:
				self.action = None
				g.on_center = True
	
	def go_on(self):
		g.on_center = False
		if self.animation != self.walk:
			self.step = 0
			self.animation = self.walk
		if g.milliseconds == 0:
			if (self.pos[0] < 580 and self.side == 'left') \
			or (self.pos[0] > -120 and self.side == 'right'):
				self.pos[0] -= 3*g.sides[self.side]['number']
			else:
				#self.action = arrive
				#if self.side == 'left':
				#	self.pos[0] = -110
				#elif self.side == 'right':
				#	self.pos[0] = 580 
				self.action = None
	
	def update_status(self):
		return g.font.render("$: %d".ljust(30) % self.money + " Rank: %d" % int(self.rank) ,1, (0,0,0))


class Robot():
	size = (285,350)
	def __init__(self, owner, gender = 'rodent', stage = 'one', color = 'natural'):
		self.owner = owner
		if self.owner.side =='left':
			self.pos = (0,0)
		else:
			self.pos = (285,0)
		self.gender = gender
		self.color = color
		self.stage = stage
		attributes = ['attack','enter','leave','lose','ouch','stay']
		dir_actions = os.path.join(g.dir_images,'robots', gender, stage, color)
		for i in attributes:
			print i
			print "  "+self.owner.side
			if self.owner.side == 'right':
				self.__dict__[i] = pygame.transform.flip(pygame.image.load(os.path.join(dir_actions, i+'.png')).convert_alpha(), 1,0)
			else:
				self.step = 0
				self.__dict__[i] = pygame.image.load(os.path.join(dir_actions, i+'.png')).convert_alpha()
		self.animation = self.enter
		if self.owner.side == 'right':
			self.step = self.animation.get_width()-self.size[0]
		else:
			self.step = 0
		self.weapons = ['fire']#TODO: include weapons here
		self.selected_weapon = 0
		self.owner.robots.append(self)
		
	def on_loop(self):
		if g.milliseconds == 0:
			if self.owner.side == 'right':
				if self.step > 0:
					self.step -= self.size[0]
				else:
					self.step = self.animation.get_width()-self.size[0]
					self.animation = self.stay
			else:
				if self.step < self.animation.get_width()-self.size[0]:
					self.step += self.size[0]
				else:
					self.step = 0
					self.animation = self.stay

	def action_attack(self):
		self.step = 0
		self.animation = self.attack

	def choose_me(self):
		self.owner.chosen_bobot = self
		
		

class InformationPanel():
	def __init__(self, panel):
		folder = os.path.join(g.dir_images, 'extras', panel)
		self.animation = [pygame.image.load(os.path.join(folder, i)) for i in sorted(os.listdir(folder))]
		self.pos = (0,0)
		self.step = 0
		self.image = self.animation[self.step]
		self.count = 0

	def on_loop(self):
		if g.milliseconds == 0:
			if self.count > 90:
				self.image = self.animation[self.step]
				if self.step < len(self.animation):
					self.step +=1
			else:	
				self.count +=1
