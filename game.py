import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
import bullet as bl
import alien

def run_game():
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    alien.create_fleet(ai_settings, screen, aliens)

    while True:
        gf.check_events(screen, ship, bullets)

        ship.update()
        
        bl.update_bullets(bullets, aliens, ai_settings)

        gf.draw_screen(ai_settings, screen, ship, bullets, aliens)

if __name__ == "__main__":
    run_game()