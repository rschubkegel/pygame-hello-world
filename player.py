import pygame
from pygame.locals import *
from regular_spritesheet import *


class Player():


    MOVE_X_SPEED = 5
    MAX_Y_SPEED = 20
    JUMP_SPEED = 15
    GRAVITY = 0.7


    '''
    pos:        a tuple with x & y coordinates where the player starts
    sheet:      a regular sprite sheet from which to load player images
    '''
    def __init__(self, pos, sheet):
        super().__init__()
        self.speed = pygame.math.Vector2(0, 0)
        self.frames = []
        for i in range(2):
            self.frames.append(sheet.get_image(0 + i, 0))
        self.rect = self.frames[0].get_rect()
        self.rect.center = pos
        self.moving_right = True
        self.jumping = False


    def update(self):
        keys = pygame.key.get_pressed()
        self.move_x(keys)
        self.move_y(keys)
        self.rect.move_ip(self.speed)
        self.bounce(pygame.display.Info().current_h)


    '''
    keys:       the keys being pressed (to check for L/R movement)
    '''
    def move_x(self, keys):

        # don't move if keys aren't pressed
        self.speed[0] = 0

        if keys[K_RIGHT]:
            self.speed[0] += self.MOVE_X_SPEED
            self.moving_right = True
        if keys[K_LEFT]:
            self.speed[0] -= self.MOVE_X_SPEED
            self.moving_right = False


    '''
    keys:       the keys being pressed (to check for jumping)
    '''
    def move_y(self, keys):

        # gravity
        self.speed[1] += self.GRAVITY
        if self.speed[1] > self.MAX_Y_SPEED:
            self.speed[1] = self.MAX_Y_SPEED

        # jump
        if keys[K_UP] and not self.jumping:
            self.speed[1] = -self.JUMP_SPEED
            self.jumping = True


    '''
    floor_y:    the y coordinate where the player should bounce
    bouciness:  how much the character should bounce,
                0 is none and 1 bounces full velocity
    '''
    def bounce(self, floor_y, bounciness=0):
        if self.rect.bottom > floor_y:
            self.rect.bottom = floor_y
            self.speed[1] *= -bounciness
            self.jumping = False


    '''
    screen:     the screen that will blit the player
    '''
    def display(self, screen):

        # by default, just show first frame (character standing/floating)
        # but if character is moving and on the ground, play animation
        frame = self.frames[0] 
        if abs(self.speed[0]) > 0.1 and not self.jumping:
            frame = self.frames[pygame.time.get_ticks() // 180 % len(self.frames)]
        if self.moving_right:
            frame = pygame.transform.flip(frame, True, False)
        screen.blit(frame, self.rect)