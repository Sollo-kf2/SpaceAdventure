import pygame

class Settings():
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.caption = "Alien Invasion"
        self.bg = pygame.image.load('images/space.jpg')
        self.bg_rect = self.bg.get_rect()