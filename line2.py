
# Drawing Lines

import sys
import pygame
from pygame.locals import *
pygame.init()


screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Lines")


while True:
    for even in pygame.event.get():
        if even.type in (QUIT, KEYDOWN):
            sys.exit()
            
    screen.fill((0, 80, 0))
    
    #Draw the line
    color = 100, 255, 200
    width = 8
    pygame.draw.line(screen, color, (100, 100), (500, 400), width)
    
    pygame.display.update()
