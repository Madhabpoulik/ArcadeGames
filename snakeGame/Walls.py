import pygame
from constants import *

class Walls(object):
    def createList(self, size):
        walls = []
        walls.append(pygame.Rect((0,0), (window_w, size)))
        walls.append(pygame.Rect((0,window_h - size), (window_w, size)))
        return walls
        