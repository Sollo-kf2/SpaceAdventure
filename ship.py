from pygame.image import load
from pygame.transform import smoothscale
from pygame.transform import rotate
from pygame.sprite import Sprite
import math

class Ship(Sprite):

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        
        super(Ship, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.acceleration = 0.06
        self.speed = 0
        self.max_speed = 3
        self.angle_speed = 1
        self.current_direction = [0, -1]
        self.current_angle = 0
        
        # Load the ship image and get its rect.
        self.image = load('images/ships/Ships3/ship1.png')
        self.rect = self.image.get_rect()
        self.image = smoothscale(self.image, (self.rect.width / 3, self.rect.height / 3))
        self.rect = self.image.get_rect()

        self.original = self.image.copy()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.rotate_right = False
        self.rotate_left = False
        
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

    def update(self):
        """Update the ship's position based on the movement flag."""

        if self.rotate_right or self.rotate_left:
            if self.rotate_right:
                self.current_angle = (self.current_angle - self.angle_speed) % 360
            if self.rotate_left:
                self.current_angle = (self.current_angle + self.angle_speed) % 360

            self.image = rotate(self.original, self.current_angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        self.update_direction()

        if (self.moving_up or self.moving_down) and not self.is_speed_max():
            if self.moving_up:
                self.speed -= self.acceleration
                
            if self.moving_down:
                self.speed += self.acceleration
        elif self.speed:
            if self.speed >= -0.001 and self.speed <= 0.001:
                self.speed = 0
            elif self.speed > 0:
                self.speed -= self.acceleration
            elif self.speed < 0:
                self.speed += self.acceleration

        if self.speed:
            self.centery += self.speed * self.current_direction[1]
            self.centerx += self.speed * self.current_direction[0]

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 