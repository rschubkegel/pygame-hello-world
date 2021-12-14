# import packages
import pygame, sys
from pygame.locals import *
from spritesheet.regular_spritesheet import *
from player import *
from tile_map import *


# initialize game engine
pygame.init()

# create pygame variables
screen_width = pygame.display.Info().current_w - 50
screen_height = pygame.display.Info().current_h - 100
screen = pygame.display.set_mode((screen_width, screen_height))
scale = 3
clock = pygame.time.Clock()

# create game variables
player = Player( \
    (screen_width // 2, screen_height // 2), \
    RegularSpritesheet("imgs/characters_packed.png", 24, scale))
tile_map = TileMap( \
    RegularSpritesheet("imgs/tiles_packed.png", 18, scale), \
    file_path="levels/level0.csv", \
    pos=(screen_width // 2, (screen_height // 2) + 100))


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
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit_game()

        # physics
        clock.tick(60)
        player.update(tile_map.tile_group)
        tile_map.update((0, 0))

        # display
        screen.fill((30, 50, 80))
        tile_map.display(screen)
        player.display(screen)
        pygame.display.flip()


# run game
if __name__ == "__main__":
    main()