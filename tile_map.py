import pygame, pandas
from regular_spritesheet import *


class TileMap:


    # 2D list of tiles
    tile_group = None


    '''
    sheet:      a regular sprite sheet from which to load tiles
    file_path:  a file from which to load level data;
                if this is not given, tile map *will* randomly generate
    pos:        a tuple with x,y values of the bottom-left position of the map
    '''
    def __init__(self, sheet, file_path=None, pos=(0, 0)):

        # initialize sprite group
        self.tile_group = pygame.sprite.Group()

        # load data from file
        if file_path:
            self.load_from_file(sheet, file_path, pos)

        # no data given; generate level
        else:
            pass


    '''
    sheet:      a regular sprite sheet from which to load tiles
    file_path:  a file from which to load level data;
                if this is not given, tile map *will* randomly generate
    pos:        a tuple with x,y values of the bottom-left position of the map
    '''
    def load_from_file(self, sheet, file_path, pos):

        # load data from CSV
        level_data = pandas.read_csv(file_path, header=None, dtype=str)

        # iterate through rows
        row_count = 2
        # TODO set row count to number of rows from CSV
        for i, data in level_data.iterrows():

            # iterate through columns
            j = 0
            for item in data:

                # calculate image col,row in sprite sheet from CSV cell
                # (cells are formatted with two letters: aa, bb, etc.
                #  where a = 0, b = 2, etc.)
                sheet_col = ord(item[0]) - ord("a")
                sheet_row = ord(item[1]) - ord("a")
                tile_img = sheet.get_image(sheet_col, sheet_row)

                # calculate tile rectangle
                tile_rect = tile_img.get_rect()
                tile_rect.left = pos[0] + (j * tile_rect.width)
                tile_rect.bottom = pos[1] - ((row_count - 1) * \
                    tile_rect.height) + (i * tile_rect.height)

                # add tile to sprite group
                self.tile_group.add(Tile(tile_img, tile_rect))

                j += 1


    '''
    offset:     a tuple with x,y values by which to move entire map
    '''
    def update(self, offset):
        for tile in self.tile_group:
            tile.rect.move_ip(offset)


    '''
    screen:     the screen that will blit the tiles
    '''
    def display(self, screen):
        self.tile_group.draw(screen)


class Tile(pygame.sprite.Sprite):


    '''
    image:      the image of this Sprite
    rect:       the rectangle of this Sprite
    '''
    def __init__(self, image, rect):
        super().__init__()
        self.image = image
        self.rect = rect