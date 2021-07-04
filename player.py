import pygame
from pygame.locals import *
from regular_spritesheet import *

class Player():

    def __init__(self, pos, spritesheet):
        super().__init__()
        self.speed = pygame.math.Vector2(0, 0)
        self.frames = []
        for i in range(2):
            self.frames.append(spritesheet.get_image(6 + i, 2))
        self.rect = self.frames[0].get_rect()
        self.rect.center = pos

    def update(self):
        pass

    def display(self, screen):
        screen.blit( \
            self.frames[pygame.time.get_ticks() // 120 % len(self.frames)], \
            self.rect)