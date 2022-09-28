import pygame
from pygame.sprite import Sprite
from pygame.transform import rotate

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, screen, ship):
        """Create a bullet object at the ship's current position."""
        
        super(Bullet, self).__init__()

        self.screen = screen
        self.bullet_width = 5
        self.bullet_height = 5
        self.color = (255, 10, 10)
        self.speed = 2

        self.image = pygame.Surface((self.bullet_width, self.bullet_height), pygame.SRCALPHA).convert_alpha()
        pygame.draw.ellipse(self.image, self.color, (0, 0, self.bullet_width, self.bullet_height))

        self.direction = ship.current_direction.copy()

        # self.image = rotate(self.image, ship.current_angle)
        self.rect = self.image.get_rect()

        # Create a bullet rect at (0, 0) and then set correct position.
        # self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""

        # Update the decimal position of the bullet.
        # self.y -= self.speed
        # Update the rect position.

        self.y += self.speed * -self.direction[1]
        self.x += self.speed * -self.direction[0]

        self.rect.x = self.x
        self.rect.y = self.y

    # def draw_bullet(self):
    #     """Draw the bullet to the screen."""
    #     pygame.draw.rect(self.screen, self.color, self.rect)

    def blitme(self):
        """Draw the alien at its current location."""

        self.screen.blit(self.image, self.rect)
        