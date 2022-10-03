from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import rotate
from pygame.transform import smoothscale
import pygame
from pygame.color import THECOLORS
import random
from pygame.sprite import Group


class Asteroid(Sprite):
    
    def __init__(self, ai_settings, screen, xpos, ypos):

        super(Asteroid, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = load('images/ships/Ships1/RD2.png')
        self.rect = self.image.get_rect()
        self.image = smoothscale(self.image, (self.rect.width / 6, self.rect.height / 6))
        self.image = rotate(self.image, 180)
        self.rect = self.image.get_rect()

        self.rect.centerx = xpos
        self.rect.centery = ypos

        self.health = 50
        self.max_health = 50
        self.health_height = 5
        self.health_bar_shift = 6

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.direction = (0, 1)
        self.speed = 1
        self.damage = 25

    def update(self):
        self.centerx += self.speed * self.direction[0]
        self.centery += self.speed * self.direction[1]
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def draw_health_bar(self):
        if self.health < 0:
            self.health = 0
        
        fill = (self.health / self.max_health) * self.rect.width

        outline_rect = pygame.Rect(self.rect.left, self.rect.top + 5, self.rect.width, self.health_height)
        fill_rect = pygame.Rect(self.rect.left, self.rect.top + 5, fill, self.health_height)

        pygame.draw.rect(self.screen, THECOLORS['red'], fill_rect)
        pygame.draw.rect(self.screen, THECOLORS['white'], outline_rect, 1)

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.draw_health_bar()

def update_asteroids(ship, asters, settings, screen):
    if len(asters) == 0:
        ast = Asteroid(settings, screen, 0, 0) #костыль
        generate_asters(settings, screen, asters, ast.rect.width, ast.rect.height)

    for aster in asters.copy():
        if aster.rect.top >= settings.screen_width:
            asters.remove(aster)

    collide = pygame.sprite.spritecollide(ship, asters, False)
    for ast in collide:
        if ship.health <= ast.damage:
            print("wasted")
        else:
            ship.health -= ast.damage
        asters.remove(ast)
    
    asters.update()

def generate_asters(ai_settings, screen, asters, aster_width, aster_height):
    num_asteroids = random.randint(1, 20)

    start_xpos = int(0 + aster_width / 2)
    end_xpos = int(ai_settings.screen_width - aster_width / 2)  

    for i in range(num_asteroids):
        xpos = random.randint(start_xpos, end_xpos + 1)
        ypos = random.randint(1, 50)
        aster = Asteroid(ai_settings, screen, xpos, -ypos)
        asters.add(aster)