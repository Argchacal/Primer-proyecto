
import pygame
from .config import *
import os


class Player (pygame.sprite.Sprite):

    def __init__(self, left, bottom, dir_images):
        pygame.sprite.Sprite.__init__(self)
        self.image_run = (pygame.image.load(os.path.join(dir_images, "Run__000.png")),
                          pygame.image.load(os.path.join(
                              dir_images, "Run__001.png")),
                          pygame.image.load(os.path.join(
                              dir_images, "Run__002.png")),
                          pygame.image.load(os.path.join(
                              dir_images, "Run__003.png")),
                          pygame.image.load(os.path.join(
                              dir_images, "Run__004.png")),
                          pygame.image.load(os.path.join(
                              dir_images, "Run__005.png")),
                          pygame.image.load(os.path.join(
                              dir_images, "Run__006.png")),
                          pygame.image.load(os.path.join(
                              dir_images, "Run__007.png")),
                          pygame.image.load(os.path.join(
                              dir_images, "Run__008.png")),
                          pygame.image.load(os.path.join(dir_images, "Run__009.png")))

        self.images = (pygame.image.load(os.path.join(dir_images, "player.png")),
                       pygame.image.load(os.path.join(
                           dir_images, "salto__001.png")),
                       pygame.image.load(os.path.join(
                           dir_images, "salto__002.png")),
                       pygame.image.load(os.path.join(
                           dir_images, "salto__003.png")),
                       pygame.image.load(os.path.join(
                           dir_images, "salto__005.png")),
                       pygame.image.load(os.path.join(
                           dir_images, "salto__006.png")),
                       pygame.image.load(os.path.join(
                           dir_images, "salto__007.png")),
                       pygame.image.load(os.path.join(
                           dir_images, "salto__008.png")),
                       pygame.image.load(os.path.join(dir_images, "salto__009.png")))

        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
        self.pos_y = self.rect.bottom  # no  da la posicion en y
        self.vel_y = 0
        self.can_jump = False
        self.playing = True
        self.step_cont = 0

    def update_pos(self):
        self.vel_y += player_grab  # esto vendria hacer la velocidad
        self.pos_y += self.vel_y + 0.5 * player_grab

    def update(self):
        if self.playing:

            self.update_pos()  # ejecutamos el metodo y actualizamos bottom q es la pos de player
            self.rect.bottom = self.pos_y

    # este metodo hace q se detenga cuando toca el suelo

    def validate_platform(self, platform):
        # nos da True si colicionan los dos colaider
        result = pygame.sprite.collide_rect(self, platform)
        if result:
            self.vel_y = 0
            self.pos_y = platform.rect.top
            self.can_jump = True
            self.image = self.images[0]
            self.play_run()
            if self.step_cont >= 9:
                self.step_cont = 0

    def play_run(self):  # modulo de caminar
        self.image = self.image_run[self.step_cont]
        self.run_rect = self.image.get_rect()
        self.run_rect.x = self.rect.bottom
        self.run_rect.y = self.pos_y
        self.step_cont += 1

    def jump(self):
        if self.can_jump:

            self.vel_y = -23
            self.can_jump = False
            for i in range(1, 9):
                self.image = self.images[i]

    def collide_with(self, sprites):
        # nos retorna una lista de objetos con los que alla colicionado
        objects = pygame.sprite.spritecollide(self, sprites, False)
        if objects:
            return objects[0]

    def stop(self):
        self.playing = False

    def collide_bottom(self, wall):
        return self.rect.colliderect(wall.rect_top)

    def skid(self, wall):
        self.pos_y = wall.rect.top
        self.vel_y = 0
        self.can_jump = True
        self.image = self.images[0]
        self.play_run()
        if self.step_cont >= 9:
            self.step_cont = 0
