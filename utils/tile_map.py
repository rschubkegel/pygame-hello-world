import pygame, pandas
from utils.spritesheet.regular_spritesheet import *


class TileMap:
    '''Represents a 2D array of game tiles.'''


    def __init__(self, sheet: RegularSpritesheet, file_path: str, pos: tuple[int, int] = (0, 0)) -> None:
        '''
        Initializes the tile map, including loading from a file.

        sheet:      a regular sprite sheet from which to load tiles
        file_path:  a file from which to load level data
        pos:        a tuple with x,y values of the center of the map
        '''

        # initialize sprite group
        self.tile_group = pygame.sprite.Group()

        # load data from file
        self._load_from_file(sheet, file_path, pos)


    def _load_from_file(self, sheet: RegularSpritesheet, file_path: str, pos: tuple[int, int]) -> None:
        '''
        Loads a grid of tiles from a CSV file. The tile images are loaded
        from a sprite sheet according to a two-letter code corresponding
        to the column and row in the sprite sheet. E.g. 'aa' corresponds
        to column index 0, row index 0.

        Parameters
        - sheet:     a regular sprite sheet from which to load tiles
        - file_path: a file from which to load level data
        - pos:       a tuple with x,y values of the center of the map
        '''

        # load data from CSV
        level_data = pandas.read_csv(file_path, header=None, dtype=str)

        # iterate through rows
        row_count = 2
        for i, data in level_data.iterrows():

            # iterate through columns
            j = 0
            col_count = len(data)
            for item in data:

                # calculate image col,row in sprite sheet from CSV cell
                # (cells are formatted with two letters: aa, bb, etc.
                #  where a = 0, b = 2, etc.)
                sheet_col = ord(item[0]) - ord("a")
                sheet_row = ord(item[1]) - ord("a")

                # if CSV cell had two spaces instead of letters,
                # don't make a tile here
                if sheet_col >= 0:

                    # get tile image
                    tile_img = sheet.get_sprite(sheet_col, sheet_row)

                    # create tile rectangle
                    tile_rect = tile_img.get_rect()

                    # center the tiles
                    tile_rect.centerx = pos[0] \
                        - (((col_count - 1) * tile_rect.width) / 2) \
                        + (j * tile_rect.width)
                    tile_rect.centery = pos[1] \
                        - (((row_count - 1) * tile_rect.height) / 2) \
                        + (i * tile_rect.height)

                    # add tile to sprite group
                    self.tile_group.add(Tile(tile_img, tile_rect))

                j += 1


    def update(self, offset: tuple[int, int]) -> None:
        '''
        Updates tiles' position by the specified offset.

        Parameters
        - offset: a tuple with x,y values by which to move entire map
        '''

        for tile in self.tile_group:
            tile.rect.move_ip(offset)


    def display(self, screen: pygame.Surface) -> None:
        '''
        Draws the tiles to the surface.

        Parameters
        - screen: the screen that will blit the tiles
        '''
        self.tile_group.draw(screen)


class Tile(pygame.sprite.Sprite):
    '''A class for game tiles.'''


    def __init__(self, image: pygame.Surface, rect: pygame.Rect) -> None:
        '''
        Sets the tile image and rectangle.

        Parameters
        - image: the image of this Sprite
        - rect:  the rectangle of this Sprite
        '''

        super().__init__()
        self.image = image
        self.rect = rect