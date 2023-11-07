import pygame
from .config import *


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # tamaño de la plataforma y lo asignamos a una variable
        self.image = pygame.Surface((WHIDTH, 40))
        # asignamos color a la plataforma
        self.image.fill(color)
        self.rect = self.image.get_rect()  # generamos el rectangulo de la plataforma
        self.rect.x = 0  # asignamos posicion
        self.rect.y = HEIGHT - 1
