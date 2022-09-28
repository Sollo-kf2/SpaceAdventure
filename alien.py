from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import rotate
from pygame.transform import smoothscale

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

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""

        self.screen.blit(self.image, self.rect)