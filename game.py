import pygame
from pygame.sprite import Group
import game_functions as gf
from tkinter.tix import InputOnly
from settings import Settings
from ship import Ship
from alien import Alien

def run_game():
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)

    while True:
        gf.check_events(screen, ship, bullets)
        ship.update()

        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

if __name__ == "__main__":
    run_game()