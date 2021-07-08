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
    sheet:      a regular sprite sheet from which to load animations
    '''
    def __init__(self, pos, sheet):
        super().__init__()
        self.speed = pygame.math.Vector2(0, 0)
        self.load_all_animations(sheet)
        self.cur_anim = "idle"
        self.rect = self.animations[self.cur_anim][0].get_rect()
        self.rect.center = pos
        self.moving_right = True
        self.jumping = False


    '''
    sheet:      a regular sprite sheet from which to load animations
    '''
    def load_all_animations(self, sheet):
        self.animations = {}
        self.load_animation(sheet, "idle", 1, 0)
        self.load_animation(sheet, "run", 2, 0)


    '''
    sheet:      a regular sprite sheet from which to load animation frames
    name:       the name of this animation
    frame_num:  the number of frames in this animation
    row:        the row on the sprite sheet where this animation is loaded from
    '''
    def load_animation(self, sheet, name, frame_num, row):
        frames = []
        for i in range(frame_num):
            frames.append(sheet.get_image(0 + i, row))
        self.animations[name] = frames


    def update(self):

        # move
        keys = pygame.key.get_pressed()
        self.change_x_speed(keys)
        self.change_y_speed(keys)
        self.rect.move_ip(self.speed)
        self.bounce(pygame.display.Info(), 0.3)

        # update animation
        if (abs(self.speed[0]) > self.MAX_SPEED[0] * 0.9) and not self.jumping:
            self.cur_anim = "run"
        else:
            self.cur_anim = "idle"


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

        # get frame from current animation
        anim_len = len(self.animations[self.cur_anim])
        frame = pygame.time.get_ticks() // 120 % anim_len
        image = self.animations[self.cur_anim][frame]

        # flip the character if moving left
        if self.moving_right:
            image = pygame.transform.flip(image, True, False)

        # display character
        screen.blit(image, self.rect)