import game_functions as gf
import pygame
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
    ship = Ship(screen)
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        # Постоянное отображение изменений экрана
        pygame.display.flip()


run_game()
