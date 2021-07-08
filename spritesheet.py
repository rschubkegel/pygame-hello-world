import pygame


class Spritesheet:


    '''
    img_path:   the path to the image to be loaded for this sprite sheet
    '''
    def __init__(self, img_path):
        self.spritesheet = pygame.image.load(img_path)


    '''
    x:          the x coordinate where this frame appears on the image
    y:          the y coordinate where this frame appears on the image
    width:      the width of the frame
    height:     the height of the frame
    scale:      how much the image will be scaled when drawn on screen
    '''
    def get_image(self, x, y, width, height, scale=1):
        image = pygame.Surface([width, height])
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image.set_colorkey(image.get_at((0, 0)))
        return pygame.transform.scale(image, (width * scale, height * scale))