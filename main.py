# Coded by Rylan Schubkegel: https://github.com/rschubkegel
# Sprites by Kenny: https://kenney.nl/assets/pixel-platformer


# import packages
import pygame, sys
from pygame.locals import *
from regular_spritesheet import *
from player import *


# initialize game engine
pygame.init()

# create pygame variables
screen_width = pygame.display.Info().current_w - 50
screen_height = pygame.display.Info().current_h - 100
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# create game variables
player = Player((screen_width // 2, screen_height // 2), \
    RegularSpritesheet("imgs/characters_packed.png", 24, 3))


# initialize the game
def init_game():
    pass


# closes the game
def quit_game():
    sys.exit()


# main game function
def main():

    init_game()

    while True:

        # user input
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()

        # physics
        clock.tick(60)
        player.update()

        # display
        screen.fill((30, 50, 80))
        player.display(screen)
        pygame.display.flip()


# run game
if __name__ == "__main__":
    main()