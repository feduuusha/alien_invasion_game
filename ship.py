import pygame


class Ship:

    def __init__(self, screen):
        """Инициализируем корабль и задаем его начальную позицию"""
        self.screen = screen
        self.image = pygame.image.load('images\\rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitime(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
