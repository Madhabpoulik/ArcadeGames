import pygame
import os
#window_size
window_w = 720
window_h = 480

#defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(0, 255, 0)
green  = pygame.Color(0, 130, 255)

#fonts
Large_font = ("Tahoma", 55)
Norm_Font =  ("Verdana", 10)
Score_Font = ("Tahoma", 20)

cell_size= 10
col_count = window_w // cell_size
row_count = window_h // cell_size

image = r'../images/snakebody.png'
#image = os.path.join("images", "snakebody.png")
