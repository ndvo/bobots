import pygame as p
tela=p.display.set_mode((800,500))
img='data/images/favicon.png'
load = p.image.load

class Bola():
	def __init__(self):
		self.vpos=[0,0]
		self.pos=[0,0]	
		self.img= load(img).convert()
		self.modelo=self.img
		self.speed=5
		self.rotacao=0

	def principal(self):
		self.vpos[0]+=self.speed
		if self.vpos[0]>800:
			self.vpos[0]=-50
		self.rotacao-=5
		if self.rotacao== 360:
			self.rotacao=0
		self.img = p.transform.rotate(self.modelo, self.rotacao)
		size = self.img.get_height()
		self.pos[1]=0-(size-70)/2
		size= self.img.get_width()
		self.pos[0]=self.vpos[0]-(size-68)/2

bola=Bola()
relogio=p.time.Clock()

while True:
	bola.principal()
	tela.blit(bola.img,bola.pos)
	p.display.flip()
	tela.fill((255,255,255))
	relogio.tick(30)
