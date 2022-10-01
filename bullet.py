import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, screen, ship):
        """Create a bullet object at the ship's current position."""
        
        super(Bullet, self).__init__()

        self.screen = screen
        self.bullet_width = 5
        self.bullet_height = 5
        self.color = (255, 10, 10)
        self.speed = 4
        self.damage = 25

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
        
def update_bullets(bullets, aliens, settings):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 or \
           bullet.rect.top >= settings.screen_height or \
           bullet.rect.right <= 0 or \
           bullet.rect.left >= settings.screen_width:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, False)
    for bul in collisions:
        if collisions[bul][0].health <= bul.damage:
            aliens.remove(collisions[bul][0])
        else:
            collisions[bul][0].health -= bul.damage 

    bullets.update()