from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import rotate
from pygame.transform import smoothscale
import pygame
from pygame.color import THECOLORS

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""

        super(Alien, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = load('images/ships/Ships1/RD1.png')
        self.rect = self.image.get_rect()
        self.image = smoothscale(self.image, (self.rect.width / 3, self.rect.height / 3))
        self.image = rotate(self.image, 180)
        self.rect = self.image.get_rect()

        self.health = 100
        self.health_height = 5

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact position.
        self.x = float(self.rect.x)
    

    def draw_health_bar(self):
        if self.health < 0:
            self.health = 0
        
        fill = (self.health / 100) * self.rect.width

        outline_rect = pygame.Rect(self.rect.left, self.rect.top + 5, self.rect.width, self.health_height)
        fill_rect = pygame.Rect(self.rect.left, self.rect.top + 5, fill, self.health_height)

        pygame.draw.rect(self.screen, THECOLORS['red'], fill_rect)
        pygame.draw.rect(self.screen, THECOLORS['white'], outline_rect, 1)

    def draw(self):
        """Draw the alien at its current location."""

        self.screen.blit(self.image, self.rect)
        self.draw_health_bar()