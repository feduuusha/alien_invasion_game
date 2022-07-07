import game_functions as gf
import pygame
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
    # Создание группы для хранения пуль
    bullets = Group()
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        # Постоянное отображение изменений экрана
        pygame.display.flip()


run_game()
