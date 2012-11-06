import pygame

class Sprite():
	def __init__(path, size, side,empty_tiles=None):
		base_image = pygame.image.load(path).convert()
		base_image_size = base_image.get_size()
		cols = base_image_size[0]/size[0]
		rows = base_image_size[1]/size[0]
		if base_image_size[0]%cols o



