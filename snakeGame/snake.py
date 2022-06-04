import pygame
from constants import *

class Snake(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__int__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))
        self.body = [[col_count // 2, row_count // 2],
                     [col_count // 2, row_count // 2 + 1],
                     [col_count // 2, row_count // 2 + 2]]
        self.direction = [-1, 0]
        self.old_key = ""
        self.speed = 10
        self.lives = 5
        self.points = 0
    
    def set_direction(self, key):
        if self.old_key == key:
            self.speed = 20
        
        if key == pygame.K_UP and self.direction != [0,1]:
            