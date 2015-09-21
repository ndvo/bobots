if __name__ =="__main__":
	import testing

import pygame
import g
import os

class Sprite():
	def __init__(self, path, size, side,empty_tiles=0):
		self.empty_tiles = empty_tiles
		self.side = side
		if side == "right":
			self.image = pygame.transform.flip(pygame.image.load(path).convert_alpha(),1,0)
		else:
			self.image = pygame.image.load(path).convert_alpha()
		self.image_size = self.image.get_size()
		self.cols = self.image_size[0]/size[0]
		self.rows = self.image_size[1]/size[0]
		self.size = size
		assert self.image_size[0]%self.cols == 0
		self.reset_step()
		print self.cols, self.rows, self.empty_tiles
		self.total_steps = (self.cols*self.rows)-self.empty_tiles
		self.step_no = 0

	
	def reset_step(self):
		if self.side =='right':
			self.step = [self.image_size[0]-self.size[0], self.image_size[1]-self.size[1]]
		else:
			self.step = [0,0]
		
	def on_loop(self):
		"""Return true if the animation reaches it's end."""
		done_animation = False
		if g.milliseconds == 0:
			done_animation = self.next_step()
		if done_animation:
			return True

	def next_step(self):
		end = False
		row_end = False
		last_row = False
		self.step_no+=1
		if self.step[1] == self.image_size[1]-self.size[1]:
			last_row = True
		if self.side == 'right' :
			if self.step[0] == 0 \
			or (self.empty_tiles and last_row and self.step[0]==self.empty_tiles*self.size[0]):
				self.step[0] = self.image_size[0]-self.size[0]
				row_end = True
			else:
				self.step[0] -= self.size[0]
		elif self.side == 'left':
			if self.step[0] == self.image_size[0]-self.size[0]:
				self.step[0] = 0
				row_end = True
			else:
				self.step[0] += self.size[0]
		if row_end:
			if self.step[1] < self.image_size[1]-self.size[1]:
				self.step[1] += self.size[1]
			else:
				self.step[1] = 0
			if last_row:
				self.step_no=0
				#self.step[1] = 0
				end = True
		return end


if __name__ =="__main__":
	import testing
	import pygame
	import g
	surface = pygame.display.set_mode((800,600))	
	testando = Sprite(
		os.path.join(g.dir_images, 'robots','rodent','two','natural','enter.png'),
		(285,350),
		'right',
		)
	while True:	
		surface.fill((0,0,0,0))
		surface.blit(testando.image, (0,0),(testando.step, testando.size))
		pygame.display.flip()
		testing.clock.tick(40)
		if testando.on_loop():
			print "fim"

