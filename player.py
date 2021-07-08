import pygame
from pygame.locals import *
from regular_spritesheet import *


class Player():


    # how fast player moves L/R, how fast player can fall
    MAX_SPEED = (7, 20)

    # L/R acceleration when key pressed, gravity
    MOVE_SPEED = 1.2

    # L/R deceleration; 0 is instant and 1 is no deceleration
    DECEL = 0.9

    # gravity
    GRAVITY = 0.7

    # how fast y speed is when up key pressed
    JUMP_SPEED = 15


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
        self.change_x_speed(keys)
        self.change_y_speed(keys)
        self.rect.move_ip(self.speed)
        self.bounce(pygame.display.Info(), 0.3)


    '''
    keys:       the keys being pressed (to check for L/R movement)
    '''
    def change_x_speed(self, keys):

        # adjust speed L/R keys are pressed
        if keys[K_RIGHT]:
            self.speed[0] += self.MOVE_SPEED
            self.moving_right = True

        if keys[K_LEFT]:
            self.speed[0] -= self.MOVE_SPEED
            self.moving_right = False

        # no move key pressed; decelerate
        if not (keys[K_RIGHT] or keys[K_LEFT]):
            self.speed[0] *= self.DECEL

        # cap speed
        if self.speed[0] > self.MAX_SPEED[0]:
            self.speed[0] = self.MAX_SPEED[0]

        elif self.speed[0] < -self.MAX_SPEED[0]:
            self.speed[0] = -self.MAX_SPEED[0]


    '''
    keys:       the keys being pressed (to check for jumping)
    '''
    def change_y_speed(self, keys):

        # gravity
        self.speed[1] += self.GRAVITY
        if self.speed[1] > self.MAX_SPEED[1]:
            self.speed[1] = self.MAX_SPEED[1]

        # jump
        if keys[K_UP] and not self.jumping:
            self.speed[1] = -self.JUMP_SPEED
            self.jumping = True


    '''
    screen_info:    object from which to get bounds of window
    bouciness:      how much the character should bounce,
                    0 is none and 1 bounces full velocity
    '''
    def bounce(self, screen_info, bounciness=0):

        # stop on L/R sides of screen
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed[0] *= -bounciness

        elif self.rect.right > screen_info.current_w:
            self.rect.right = screen_info.current_w
            self.speed[0] *= -bounciness

        # bounce on bottom of screen
        if self.rect.bottom > screen_info.current_h:
            self.rect.bottom = screen_info.current_h
            self.speed[1] *= -bounciness
            self.jumping = False


    '''
    screen:     the screen that will blit the player
    '''
    def display(self, screen):

        # by default, just show first frame (character standing/floating)
        frame = self.frames[0]

        # if character is moving and on the ground, play animation
        if abs(self.speed[0]) > 1.0 and not self.jumping:
            frame = self.frames[pygame.time.get_ticks() // 120 % len(self.frames)]

        # flip the character if moving left
        if self.moving_right:
            frame = pygame.transform.flip(frame, True, False)

        # display character
        screen.blit(frame, self.rect)