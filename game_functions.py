import sys
import pygame
from time import sleep
from alien import Alien
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    # Отслеживание событий клавиатуры и мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Обновляет изображения на экране и отображает новый экран"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitime()
    aliens.draw(screen)
    # Постоянное отображение изменений экрана
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, aliens, bullets, screen, ship)


def check_bullet_alien_collision(ai_settings, aliens, bullets, screen, ship):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_keydown_events(event, ai_setting, screen, ship, bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижение пришельцем края экрана"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def fire_bullet(ai_setting, screen, ship, bullets):
    # Создание новой пули и добавление ее в группу bullets
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def create_fleet(ai_settings, screen, ship, aliens):
    """Создаёт флот пришельцев"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # Создание ряда пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    # Рассчитываем допустимое кол-во пришельцев
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет кол-во рядом помещающихся на экране"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(1.0)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Проверяет добрались ли пришельцы до нижней части экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
