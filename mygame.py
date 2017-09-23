import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)

#initialize pygame 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My_Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()	
#game loop
running = True
while running:
	clock.tick(FPS)
	for event in pygame.event.get():
		#check for closing window
		if event.type == pygame.QUIT:
			running = False
	
	# Update
	all_sprites.update()
	# Draw/ render
	all_sprites.draw(screen)
	screen.fill(BLACK)
	pygame.dipslay.flip()
Pygame.quit()