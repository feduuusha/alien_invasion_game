import pygame
import game_functions as gf
from ship import Ship
from button import Button
from settings import Settings
from pygame.sprite import Group
from scoreboard import Scoreboard
from game_stats import GameStats


def run_game():
    # Инициализируем игру и создаем объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, 'Play')
    # Создание корабля.
    ship = Ship(ai_settings, screen)
    # Создание пришельцев
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Создание группы для хранения пуль
    bullets = Group()
    # Создание экземпляра статистики
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        # if stats.game_active:
        ship.update()
        gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
