import pygame
import random
import os
WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
#setup asets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image.fill(G)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0
    def update(self):
    	self.rect.x += self.speedx
    	self.rect.y += self.speedy
    	if self.rect.right < 0:
    		self.rect.left = WIDTH
    	elif self.rect.left > WIDTH:
    		self.rect.right = 0
    	if self.rect.bottom < 0:
    		self.rect.top = HEIGHT
    	elif self.rect.top > HEIGHT:
    		self.rect.bottom = 0

class Mob(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10,10))
		self.image.fill(R)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(HEIGHT - self.rect.height)
	def update(self):
		#some condition
		#self.rect.x = random.randrange(WIDTH - self.rect.width)
		#self.rect.y = random.randrange(HEIGHT - self.rect.height)
		pass
#initialize pygame 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My_Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
mob = Mob()
all_sprites.add(player)
all_sprites.add(mob)	
#game loop
running = True
while running:
	clock.tick(FPS)
	for event in pygame.event.get():
		#check for closing window
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.speedx = -5
				player.speedy = 0
			if event.key == pygame.K_RIGHT:
				player.speedx = 5
				player.speedy = 0
			if event.key == pygame.K_UP:
				player.speedy = -5
				player.speedx = 0
			if event.key == pygame.K_DOWN:
				player.speedy = 5
				player.speedx = 0
	# Update
	all_sprites.update()
	# Draw/ render
	
	screen.fill(BLACK)
	all_sprites.draw(screen)
	pygame.display.flip()
pygame.quit()