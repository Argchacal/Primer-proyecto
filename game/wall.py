import pygame
from .config import *
import os


class Wall(pygame.sprite.Sprite):
    def __init__(self, left, bottom, dir_images):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(
            dir_images, "wall.png"))  # genera la superficie

        self.rect = self.image.get_rect()  # genero el rectangulo para la superficie
        self.rect.left = left
        self.rect.bottom = bottom
        self.vel_x = speed
        # genera un rectangulo encima del wall
        self.rect_top = pygame.Rect(
            self.rect.x, self.rect.y, self.rect.width, 1)

    def update(self):
        self.rect.left -= self.vel_x
        # con esto siempre el rectangulo estara en la parte superior
        self.rect_top.x = self.rect.x

    def stop(self):
        self.vel_x = 0
