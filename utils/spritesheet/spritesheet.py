import pygame


class Spritesheet:
    '''
    Contains a pygame.Surface object from which
    specific frames can be extracted.
    '''


    def __init__(self, img_path: str)-> None:
        '''
        Initializes the sprite sheet.

        Parameters
        - img_path: the path to the image to be loaded for this sprite sheet
        '''

        self.spritesheet = pygame.image.load(img_path)


    def get_sprite(self, x: int, y: int, width: int, height: int, scale: int = 1) -> pygame.Surface:
        '''
        Gets a specific sprite/frame from the sprite sheet.

        - x:      the x coordinate where this frame appears on the image
        - y:      the y coordinate where this frame appears on the image
        - width:  the width of the frame
        - height: the height of the frame
        - scale:  how much the image will be scaled when drawn on screen
        '''

        image = pygame.Surface([width, height])
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0,0,0,0))
        return pygame.transform.scale(image, (width * scale, height * scale))