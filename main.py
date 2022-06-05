import pygame
import sys
from player import Player
import random
import time

RED = ((255,0,0))
GREEN = ((0,255,0))
BLUE = ((0,0,255))
YELLOW = ((255,255,0))

positions = [(208,415),(209, 386),(208, 357),(209, 329),(209, 298),(179, 270),(150, 267),(121, 266),
(88, 268),(58, 268),(31, 267),(27, 239),(34, 209),(57, 206),(89, 207),(118, 205),(145, 206),(177, 208),(210, 177),
(207, 150),(211, 120),(209, 86),(211, 62),(213, 29),(238, 31),(267, 32),(268, 55),(271, 87),(270, 117),
(270, 146),(271, 177),(301, 207),(328, 207),(359, 208),(388, 206),(413, 206),(449, 209),(453, 234),(454, 264),
(419, 265),(396, 265),(362, 266),(329, 265),(303, 266),(272, 294),(273, 330),(271, 354),(271, 387),(270, 418),
(267, 449),(240, 447),(106, 402)]


positions_blue = [(420, 267),(390, 268),(356, 268),(331, 268),(302, 269),(269, 298),(268, 327),(268, 357),
(269, 388),(267, 414),(267, 446),(238, 448),(209, 447),(208, 417),(208, 388),(208, 358),(210, 329),(209, 301),
(178, 267),(147, 267),(118, 266),(89, 267),(56, 265),(27, 266),(29, 236),(27, 207),(58, 207),(89, 205),
(119, 206),(147, 205),(177, 208),(209, 176),(206, 144),(208, 117),(208, 85),(208, 60),(211, 25),(239, 25),
(268, 25),(270, 57),(268, 86),(269, 115),(271, 145),(269, 172),(301, 203),(328, 204),(360, 205),(386, 204),
(417, 206),(447, 206),(449, 235),(421, 233),(389, 237),(361, 234),(330, 236),(300, 234),(269, 237),
]

positions_green = [(59, 204),(87, 206),(119, 204),(149, 205),(179, 205),(209, 174),(209, 145),(209, 114),
(208, 85),(208, 54),(208, 24),(240, 24),(270, 25),(269, 55),(268, 86),(269, 117),(268, 144),(269, 174),(298, 204),
(329, 206),(359, 206),(388, 205),(421, 204),(447, 206),(448, 237),(449, 265),(422, 264),(388, 264),(359, 266),
(332, 264),(300, 264),(271, 295),(268, 325),(270, 358),(270, 383),(269, 413),(268, 443),(239, 447),(207, 448),
(208, 416),(211, 385),(210, 358),(212, 323),(209, 297),(178, 268),(147, 265),(121, 268),(89, 266),(59, 265),
(27, 263),(24, 235),(60, 236),(88, 237),(120, 236),(147, 235),(177, 234),(212, 238),
]

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

sprites = pygame.sprite.Group()

player = Player(RED, 210, 450, positions)
player2 = Player(BLUE, 449, 268, positions_blue)
player3 = Player(GREEN, 28, 205, positions_green)
#player4 = Player(YELLOW, 268, 25)

sprites.add(player,player2,player3)

enemy_sprites = []
enemy_sprites.append(player2)
enemy_sprites.append(player3)

player_pos = -1

def roll_dice():
	global player_pos
	rand_num = random.randint(1,6)
	print(f"Random num {rand_num}")
	player_pos += rand_num 
	print(f"Player pos {player_pos}")
	player.rect.center = (positions[player_pos])

def roll_dice_enemy():
	for i in range(len(enemy_sprites)):
		enemy_sprites[i].roll_dice()


def draw_board_and_players():
	background_image = pygame.image.load("LudoBoardImage.png").convert()
	SCREEN.blit(background_image, [0,0])

	sprites.draw(SCREEN)
	sprites.update()

def main():
	running = True
	while running:
		draw_board_and_players()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					roll_dice()
					roll_dice_enemy()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				print(pos)
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
main()