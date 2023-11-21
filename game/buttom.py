
import pygame


class Buttom(pygame.sprite.Sprite):
    def __init__(self, image1, image2, x=200, y=200):
        self.image_normal = image1
        self.image_selection = image2
        self.image_current = self.image_normal
        self.rect = self.image_current.get_rect()
        self.rect.left = x
        self.rect.top = y

    def update(self, scream, cursor):
        if cursor.colliderect(self.rect):
            self.image_current = self.image_selection
        else:
            self.image_current = self.image_normal

        scream.blit(self.image_current, self.rect)


class Cursor(pygame.rect):
    def __init__(self):

        pygame.Rect.__init__(self, 0, 0, 1, 1)

    def update(self):
        self.left, self.top = pygame.mouse.get_pos()
