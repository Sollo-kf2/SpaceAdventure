import sys, pygame
import bullet
import alien

def check_keydown_events(event, screen, ship, bullets):
    if event.key == pygame.K_e:
        ship.moving_right = True
    if event.key == pygame.K_q:
        ship.moving_left = True
    if event.key == pygame.K_w:
        ship.moving_up = True
    if event.key == pygame.K_s:
        ship.moving_down = True

    if event.key == pygame.K_d:
        ship.rotate_right = True
    if event.key == pygame.K_a:
        ship.rotate_left = True

    if event.key == pygame.K_SPACE:
        bullet.fire_bullet(screen, ship, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_e:
        ship.moving_right = False
    if event.key == pygame.K_q:
        ship.moving_left = False
    if event.key == pygame.K_w:
        ship.moving_up = False
    if event.key == pygame.K_s:
        ship.moving_down = False

    if event.key == pygame.K_d:
        ship.rotate_right = False
    if event.key == pygame.K_a:
        ship.rotate_left = False

def check_events(screen, ship, bullets):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def draw_screen(ai_settings, screen, ship, bullets, aliens):
    """Update images on the screen and flip to the new screen."""

    screen.blit(ai_settings.bg, ai_settings.bg_rect)
    ship.blitme()
    
    for alien in aliens:
        alien.draw()

    bullets.draw(screen)
    
    pygame.display.flip()