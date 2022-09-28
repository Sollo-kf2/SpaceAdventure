import sys, pygame
from bullet import Bullet
from alien import Alien

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
        fire_bullet(screen, ship, bullets)

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

def update_screen(ai_settings, screen, ship, bullets, aliens):
    """Update images on the screen and flip to the new screen."""

    screen.blit(ai_settings.bg, ai_settings.bg_rect)
    ship.blitme()
    aliens.draw(screen)

    for bullet in bullets.sprites():
        bullet.blitme()
    
    pygame.display.flip()

def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    bullets.update()

def fire_bullet(screen, ship, bullets):
    new_bullet = Bullet(screen, ship)
    bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens."""

    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)