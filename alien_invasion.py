import game_functions as gf
import pygame
from game_stats import GameStats
from pygame.sprite import Group
from settings import Settings
from ship import Ship


def run_game():
    # Инициализируем игру и создаем объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание корабля.
    ship = Ship(ai_settings, screen)
    # Создание пришельцев
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Создание группы для хранения пуль
    bullets = Group()
    # Создание экземпляра статистики
    stats = GameStats(ai_settings)
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
