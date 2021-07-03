import pygame

class Spritesheet():
    
    def __init__(self, img_path):
        self.spritesheet = pygame.image.load(img_path)
    
    def get_image(self, x, y, width, height, scale=1):
        image = pygame.Surface([width, height])
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image.set_colorkey(image.get_at((0, 0)))
        return pygame.transform.scale(image, (width * scale, height * scale))