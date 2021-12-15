from pygame import Surface
from utils.spritesheet.spritesheet import Spritesheet


class RegularSpritesheet(Spritesheet):
    '''
    A sprite sheet with consistent resolution for each frame.
    '''


    def __init__(self, img_path, sheet_res, scale=1) -> None:
        '''
        Initializes the sprite sheet.

        Parameters
        - img_path:  the path to the sprite sheet image file
        - sheet_res: the pixel resolution of frames in the sprite sheet
        - scale:     how much to scale the sprite when drawn
        '''
        super().__init__(img_path)
        self.res = sheet_res
        self.scale = scale


    def get_sprite(self, col: int, row: int) -> Surface:
        '''
        Extracts a sprite from the sheet.

        Parameters
        - col: the column of this frame on the sprite sheet
        - row: the row of this frame on the sprite sheet

        Returns
        - a Surface object representing one sprite from this sprite sheet
        '''
        return super().get_sprite(col * self.res, row * self.res, \
            self.res, self.res, self.scale)


    def get_sprites(self, count: int, col: int, row: int, is_vertical: bool = False) -> list[Surface]:
        '''
        Gets several sprites in sequence. Perfect for populating animations.

        Parameters
        - count:       the number of sequential sprites to load
        - col:         the column index of the first sprite in the sequence
        - row:         the row index of the first sprite in the sequence
        - is_vertical: most sprite sheets read left to right so the
                       sprite sequence is expected to be horizontal by default;
                       if the sprite sheet reads top to bottom, the
                       is_vertical flag should be set to True
        '''

        frames = []
        for i in range(count):
            if not is_vertical:
                frames.append(self.get_sprite(col + i, row))
            else:
                frames.append(self.get_sprite(col, row + i))
        return frames
