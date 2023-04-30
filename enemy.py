import menu
from shared_stats import my_instance
import pygame

class Enemy:
    x_wide = 0
    y_wide= 0

    x_long = 0
    x_long_2 = 0
    y_long= 0

    speed = 0.0
    size = 25
    SQUARE_WIDTH_W = 25
    SQUARE_HEIGHT_W = 5

    SQUARE_WIDTH_L = 5
    SQUARE_HEIGHT_L = 25

    difficulty = [1,2,3]
    e_diff = 0
    my_stats = my_instance

    enemy = pygame.Rect(x_wide, y_wide, SQUARE_WIDTH_W, SQUARE_HEIGHT_W)
    enemy1 = pygame.Rect(x_long, y_long, SQUARE_WIDTH_L, SQUARE_HEIGHT_L)
    enemy2 = pygame.Rect(x_long, y_long, SQUARE_WIDTH_L, SQUARE_HEIGHT_L)



    def attack_x(self):
        if self.my_stats.POINTS >= 3:
             self.e_diff = self.difficulty[0]
             self.speed = 0.1
        if self.my_stats.POINTS >= 10:
             self.e_diff = self.difficulty[1]
             self.speed = 0.3
        if self.my_stats.POINTS >= 15:
             self.e_diff = self.difficulty[2]
             self.speed = 0.5


        if self.e_diff > 0:
            self.enemy = pygame.Rect(self.x_wide, self.y_wide, self.SQUARE_WIDTH_W, self.SQUARE_HEIGHT_W)
            self.x_wide += self.speed
            self.y_wide = 200
            if self.x_wide >= 625:
                self.x_wide = 0
            #print(self.e_diff, self.speed)

    def attack_y(self):
        if self.my_stats.POINTS >= 3:
             self.e_diff = self.difficulty[0]
             self.speed = 0.1
        if self.my_stats.POINTS >= 10:
             self.e_diff = self.difficulty[1]
             self.speed = 0.3
        if self.my_stats.POINTS >= 15:
             self.e_diff = self.difficulty[2]
             self.speed = 0.5


        if self.e_diff > 0:
            self.enemy1 = pygame.Rect(self.x_long, self.y_long, self.SQUARE_WIDTH_L, self.SQUARE_HEIGHT_L)
            self.x_long = 100
            self.y_long += self.speed
            if self.y_long >= 450:
                self.y_long = 0

    def attack_y_(self):
        if self.my_stats.POINTS >= 3:
             self.e_diff = self.difficulty[0]
             self.speed = 0.1
        if self.my_stats.POINTS >= 10:
             self.e_diff = self.difficulty[1]
             self.speed = 0.3
        if self.my_stats.POINTS >= 15:
             self.e_diff = self.difficulty[2]
             self.speed = 0.5


        if self.e_diff > 0:
            self.enemy2 = pygame.Rect(self.x_long_2, self.y_long, self.SQUARE_WIDTH_L, self.SQUARE_HEIGHT_L)
            self.x_long_2 = 500
            self.y_long += self.speed
            if self.y_long >= 450:
                self.y_long = 0

my_enemy_I = Enemy()
