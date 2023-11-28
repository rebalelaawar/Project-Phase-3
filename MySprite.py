import pygame
class MySprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x ,y):
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

all_sprites = pygame.sprite.Group()





