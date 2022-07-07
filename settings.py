

class Settings:
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        self.screen_width = 1800
        self.screen_height = 900
        self.bg_color = (117, 187, 253)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
