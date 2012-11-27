import pygame
import g

class Sprite():
	def __init__(self, path, size, side,empty_tiles=None):
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
		self.step = [0,0]
	
	def on_loop(self):
		"""Return true if the animation reaches it's end."""
		if g.milliseconds == 0:
			row_end = False
			last_row = False
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
					self.step[1] = 0
					return True



