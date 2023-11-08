
from .config import *
import pygame
import os


class Coin (pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, dir_images):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(dir_images, "coin.png"))

        self.rect = self.image.get_rect()  # genero el rectangulo de la moneda
        self.rect.x = pos_x  # Para posicionarlo en los ejes que deseo
        self.rect.y = pos_y
        self.vel_x = speed

    def update(self):
        self.rect.left -= self.vel_x

    def stop(self):
        self.vel_x = 0
