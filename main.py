# assets by Kenny: https://kenney.nl/assets/pixel-platformer

# import packages
from regular_spritesheet import RegularSpritesheet
import pygame, sys
from pygame.locals import *
from regular_spritesheet import *

# initialize game engine
pygame.init()

# create pygame variables
size = (screen_width, screen_height) = (1000, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# create game variables
frames = []

# initialize the game
def init_game():
    spritesheet = RegularSpritesheet("imgs/characters_packed.png", 24, 3)
    frames.append(spritesheet.get_image(6, 2))
    frames.append(spritesheet.get_image(7, 2))
    frames.append(spritesheet.get_image(8, 2))

# closes the game
def quit_game():
    sys.exit()

# main game function
def main():

    init_game()

    while True:

        # tick
        clock.tick(30)

        # user input
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()

        # physics

        # display
        screen.fill((50, 90, 150))
        screen.blit(frames[pygame.time.get_ticks() // 120 % len(frames)], frames[0].get_rect())
        pygame.display.flip()

if __name__ == "__main__":
    main()