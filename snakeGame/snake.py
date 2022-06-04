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
            self.direction = [0, -1]
            self.old_key = key
        
        elif key == pygame.K_DOWN and self.direction != [0,-1]:
            self.direction = [0, 1]
            self.old_key = key
        
        elif key == pygame.K_LEFT and self.direction != [1,0]:
            self.direction = [-1, 0]
            self.old_key = key
        
        elif key == pygame.K_RIGHT and self.direction != [-1, 0]:
            self.direction = [1, 0]
            self.old_key = key
        
    def move(self):
        self.body.insert(0, [self.body[0][0] + self.direction[0],
                             self.body[0][1] + self.direction[1]])
        
        self.body[0][0] = self.body[0][0] % col_count
        self.body[0][1] = self.body[0][1] % row_count
        
    def draw(self, screen):
        for elem in self.body:
            screen.blit(self.image, (elem[0] * cell_size, elem[1] * cell_size,
                                     cell_size, cell_size))
    
    def after_hit(self):
        self.lives -= 1
        
        self.body = [[col_count // 2, row_count // 2],
                     [col_count // 2, row_count // 2 + 1],
                     [col_count // 2, row_count // 2 + 2]]
        self.direction = [0, -1]       
    
    def hit_walls(self, walls):
        hit = False
        
        for wall in walls:
            head_rect = pygame.Rect(self.body[0][0] * cell_size, self[0][1] * cell_size,
                                    cell_size, cell_size)
            if(wall.colliderect(head_rect)):
                self.after_hit()
                hit = True
            if self.body[0] in self.body[1:]:
                self.after_hit()
                hit = True
        
        return hit