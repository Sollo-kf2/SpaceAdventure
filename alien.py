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
        self.image = smoothscale(self.image, (self.rect.width / 4, self.rect.height / 4))
        self.image = rotate(self.image, 180)
        self.rect = self.image.get_rect()

        self.health = 500
        self.max_health = 500
        self.health_height = 5
        self.health_bar_shift = 6

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact position.
        self.x = float(self.rect.x)
    

    def draw_health_bar(self):
        if self.health < 0:
            self.health = 0
        
        fill = (self.health / self.max_health) * self.rect.width

        outline_rect = pygame.Rect(self.rect.left, self.rect.top - self.health_bar_shift, self.rect.width, self.health_height)
        fill_rect = pygame.Rect(self.rect.left, self.rect.top - self.health_bar_shift, fill, self.health_height)

        pygame.draw.rect(self.screen, THECOLORS['red'], fill_rect)
        pygame.draw.rect(self.screen, THECOLORS['white'], outline_rect, 1)

    def draw(self):
        """Draw the alien at its current location."""

        self.screen.blit(self.image, self.rect)
        self.draw_health_bar()

def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens."""
    
    alien = Alien(ai_settings, screen) #костыль
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)