import menu
from shared_stats import my_instance
import pygame

class Enemy:
    x = 0
    y = 0

    size = 25
    SQUARE_WIDTH = 25
    SQUARE_HEIGHT = 5
    my_stats = my_instance

    enemy = pygame.Rect(x, y, SQUARE_WIDTH, SQUARE_HEIGHT)

    def attack(self):
        self.enemy = pygame.Rect(self.x, self.y, self.SQUARE_WIDTH, self.SQUARE_HEIGHT)
        if self.my_stats.POINTS >= 3:
                self.x += 0.1
                self.y = 200
                if self.x >= 625:
                    self.x = 0



my_enemy_I = Enemy()
