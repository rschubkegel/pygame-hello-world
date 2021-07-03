import spritesheet

class RegularSpritesheet(spritesheet.Spritesheet):

    '''
    img_path:   the path to the sprite sheet image file
    sheet_res:  the pixel resolution of frames in the sprite sheet
    '''
    def __init__(self, img_path, sheet_res, scale=1):
        super().__init__(img_path)
        self.res = sheet_res
        self.scale = scale
    
    def get_image(self, col, row):
        return super().get_image(col * self.res, row * self.res, \
            self.res, self.res, self.scale)
