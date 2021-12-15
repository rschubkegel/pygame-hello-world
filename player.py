from typing import Sequence
import pygame
from pygame.locals import *
from utils.animation import Animation
from utils.spritesheet.regular_spritesheet import RegularSpritesheet


class Player():
    '''A class representing a player that can jump, fall, and move L/R.'''


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


    def __init__(self, pos: tuple[int, int], sheet: RegularSpritesheet) -> None:
        '''
        Creates and initializes the player.

        Parameters
        - pos:   a tuple with x & y coordinates where the player starts
        - sheet: a regular sprite sheet from which to load animations
        '''

        super().__init__()
        self.speed = pygame.math.Vector2(0, 0)
        self.load_all_animations(sheet)
        self.cur_anim = "idle"
        self.rect = self.animations[self.cur_anim][0].get_rect()
        self.rect.center = pos
        self.moving_right = True
        self.jumping = False


    def load_all_animations(self, sheet: RegularSpritesheet) -> None:
        '''
        Loads all player-specific animations
        into a dictionary of Animation objects.

        Parameters
        - sheet: a regular sprite sheet from which to load animations
        '''

        self.animations = {}
        self.animations["idle"] = Animation(sheet.get_sprites(1, 0, 0))
        self.animations["run"] = Animation(sheet.get_sprites(2, 0, 0))


    def update(self, tiles: pygame.sprite.Group) -> None:
        '''
        Player updates (including animation).

        Parameters
        tiles: the sprite group of tiles that the player can collide with
        '''

        # move
        keys = pygame.key.get_pressed()
        self._change_x_speed(keys)
        self._change_y_speed(keys)
        self.rect.move_ip(self.speed)
        self._bounce(tiles, 0.3)

        # update animation
        if (abs(self.speed[0]) > self.MAX_SPEED[0] * 0.9) and not self.jumping:
            self.cur_anim = "run"
        else:
            self.cur_anim = "idle"


    def _change_x_speed(self, keys: Sequence[bool]) -> None:
        '''
        Updates the player's speed based on key presses.

        Parameters
        keys: the keys being pressed (to check for L/R movement)
        '''

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


    def _change_y_speed(self, keys: Sequence[bool]) -> None:
        '''
        Updates player's speed based on gravity and jumping.

        Parameters
        keys: the keys being pressed (to check for jumping)
        '''

        # gravity
        self.speed[1] += self.GRAVITY
        if self.speed[1] > self.MAX_SPEED[1]:
            self.speed[1] = self.MAX_SPEED[1]

        # jump
        if keys[K_UP] and not self.jumping:
            self.speed[1] = -self.JUMP_SPEED
            self.jumping = True


    def _bounce(self, tiles: pygame.sprite.Group, bounciness: int = 0) -> None:
        '''
        Handles collision with tiles and bouncing (if desired).

        Parameters
        tiles:     sprite group of tiles this player can collide with
        bouciness: how much the character should bounce,
                   0 is none and 1 bounces full velocity
        '''

        # collide with tiles
        for tile in pygame.sprite.spritecollide(self, tiles, False):

            # bounce off top of tiles
            if self.speed[1] >= self.rect.bottom - tile.rect.top:
                self.rect.bottom = tile.rect.top
                self.jumping = False
                self.speed[1] *= -bounciness

            # TODO bounce off sides


    def display(self, screen: pygame.surface.Surface) -> None:
        '''
        Blits the player to the specified surface.

        Parameters
        screen: the screen that will blit the player
        '''

        # get frame from current animation
        anim_len = len(self.animations[self.cur_anim])
        frame = pygame.time.get_ticks() // 120 % anim_len
        image = self.animations[self.cur_anim][frame]

        # flip the character if moving left
        if self.moving_right:
            image = pygame.transform.flip(image, True, False)

        # display character
        screen.blit(image, self.rect)