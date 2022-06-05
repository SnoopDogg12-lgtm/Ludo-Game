import pygame
import random
import time

class Player(pygame.sprite.Sprite):
    def __init__(self, color, positionx, positiony, coordinates):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.positionx = positionx
        self.positiony = positiony
        self.image = pygame.Surface((20,20))
        self.image.fill((self.color))
        self.rect = self.image.get_rect()
        self.rect.center = (self.positionx, self.positiony)
        self.player_pos = -1
        self.coordinates = coordinates
    def roll_dice(self):
        try:
            rand_num = random.randint(1,6)
            self.player_pos += rand_num
            self.rect.center = self.coordinates[self.player_pos]
        except IndexError:
            rand_num = random.randint(1,6)
    