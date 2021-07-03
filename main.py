# import packages
import pygame, sys
from pygame.locals import *

# initialize game engine
pygame.init()

# create game variables
size = (screen_width, screen_height) = (1000, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# closes the game
def quit_game():
    sys.exit()

# main game function
def main():
    while True:

        # tick
        clock.tick(60)

        # user input
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()

        # physics

        # display
        screen.fill((50, 90, 150))
        pygame.display.flip()

if __name__ == "__main__":
    main()