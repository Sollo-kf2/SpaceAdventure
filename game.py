import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
import bullet as bl
import alien
from asteroid import Asteroid
import asteroid as ast

def run_game():
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    alien.create_fleet(ai_settings, screen, aliens)
    asteroids = Group()

    while True:
        gf.check_events(screen, ship, bullets)

        ship.update(bullets)
        
        bl.update_bullets(bullets, aliens, ai_settings, asteroids, ship)
        
        gf.update_enemy_state(aliens)

        ast.update_asteroids(ship, asteroids, ai_settings, screen)

        gf.draw_screen(ai_settings, screen, ship, bullets, aliens, asteroids)

if __name__ == "__main__":
    run_game()
