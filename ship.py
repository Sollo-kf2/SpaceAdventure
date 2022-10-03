from pygame.image import load
from pygame.transform import smoothscale
from pygame.transform import rotate
from pygame.sprite import Sprite
import math
from pygame.color import THECOLORS
import pygame
import bullet

class Ship(Sprite):

    def __init__(self, screen, settings):
        """Initialize the ship and set its starting position."""
        
        super(Ship, self).__init__()

        self.settings = settings

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.acceleration = 0.05
        self.speed = 0
        self.max_speed = 2
        self.angle_speed = 1
        self.current_direction = [0, -1]
        self.current_angle = 0
        
        # Load the ship image and get its rect.
        self.image = load('images/ships/Ships3/ship1.png')
        self.rect = self.image.get_rect()
        self.image = smoothscale(self.image, (self.rect.width / 4, self.rect.height / 4))
        self.rect = self.image.get_rect()

        self.original = self.image.copy()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        self.collideRect = self.rect.copy()

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.shooting = False

        self.rotate_right = False
        self.rotate_left = False

        self.health = 50
        self.max_health = 50
        self.health_height = 5
        self.health_bar_shift = 6

        self.score = 0

    def draw_health_bar(self):
        if self.health < 0:
            self.health = 0
        
        fill = (self.health / self.max_health) * self.collideRect.width

        outline_rect = pygame.Rect(self.collideRect.left, self.collideRect.top - self.health_bar_shift, self.collideRect.width, self.health_height)
        fill_rect = pygame.Rect(self.collideRect.left, self.collideRect.top - self.health_bar_shift, fill, self.health_height)

        pygame.draw.rect(self.screen, THECOLORS['red'], fill_rect)
        pygame.draw.rect(self.screen, THECOLORS['white'], outline_rect, 1)
        
    def update_direction(self):
        self.current_direction[0] = math.sin(math.radians(self.current_angle))
        self.current_direction[1] = math.cos(math.radians(self.current_angle))
        
    def is_speed_max(self):
        if self.speed > self.max_speed:
            self.speed = self.max_speed
            return True
        elif self.speed < -self.max_speed:
            self.speed = -self.max_speed
            return True
        return False

    def update_rotation(self):
        if self.rotate_right or self.rotate_left:
            if self.rotate_right:
                self.current_angle = (self.current_angle - self.angle_speed) % 360
            if self.rotate_left:
                self.current_angle = (self.current_angle + self.angle_speed) % 360

            self.image = rotate(self.original, self.current_angle)
            self.rect = self.image.get_rect(center=self.rect.center)

    def update_speed(self):
        if (self.moving_up or self.moving_down) and not self.is_speed_max():
            if self.moving_up:
                self.speed -= self.acceleration
                
            if self.moving_down:
                self.speed += self.acceleration
        elif self.speed:
            if self.speed >= -self.acceleration and self.speed <= self.acceleration:
                self.speed = 0
            elif self.speed > 0:
                self.speed -= self.acceleration
            elif self.speed < 0:
                self.speed += self.acceleration
            
    def update_collision_with_map(self):
        # SRiNF = ship's rect in next frame

        SRiNF = self.collideRect.copy()
        if self.speed != 0:
            SRiNF.centery += self.speed * self.current_direction[1]
            SRiNF.centerx += self.speed * self.current_direction[0]

        access_to_move_x = True
        access_to_move_y = True

        if SRiNF.bottom >= self.settings.screen_height or \
           SRiNF.top <= 0:
            access_to_move_y = False
        if SRiNF.left <= 0 or \
           SRiNF.right >= self.settings.screen_width:
            access_to_move_x = False

        return access_to_move_x, access_to_move_y

    def update_position(self, access_to_move_x, access_to_move_y):
        if self.speed:
            if access_to_move_y:
                self.centery += self.speed * self.current_direction[1]
                self.rect.centery = self.centery
                self.collideRect.centery = self.rect.centery
            if access_to_move_x:
                self.centerx += self.speed * self.current_direction[0]
                self.rect.centerx = self.centerx
                self.collideRect.centerx = self.rect.centerx

    def update(self, bullets):
        """Update the ship's position based on the movement flag."""
        
        self.update_rotation()
        self.update_direction()
        self.update_speed()
        access_to_move_x, access_to_move_y = self.update_collision_with_map()
        self.update_position(access_to_move_x, access_to_move_y)
        if self.shooting:
            bullet.fire_bullet(self.screen, self, bullets)
        print("SCORE: ", self.score)

    def blitme(self):
        """Draw the ship at its current location."""

        self.screen.blit(self.image, self.rect)
        self.draw_health_bar()
        