from constants import *
from random import randrange
import pygame


class Apple:
    count = 0
    
    def __init__(self, size):
        self.x = randrange(1, col_count - 1)
        self.y = randrange(1, row_count - 1)
        self.size = size
        self.rect = pygame.Rect(self.x * cell_size, self.y * cell_size, self.size, self.size)
        
    def draw(self, screen):
        pygame.draw.rect(screen, red, self.rect)
    
    def set_random_xy(self):
        self.x = randrange(1, col_count - 1)
        self.y = randrange(1, row_count - 1)

        self.rect.x = self.x * cell_size
        self.rect.y = self.y * cell_size
        
        if(Apple.count % 3 == 0):
            self.size = cell_size + 6
            self.rect.x -= 3
            self.rect.y -= 3
        else:
            self.size = cell_size
        self.rect.width = self.size
        self.rect.height = self.size