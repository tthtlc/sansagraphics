
# Drawing Lines

import sys
import math
import pygame
from pygame.locals import *
pygame.init()


screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Rotating Lines")

PI = 3.141592653
i=0
x=100
y=100

xa=0
ya=0
n=100
theta=2*PI/n
angle=0.0
r=10
while True:
    for even in pygame.event.get():
        if even.type in (QUIT, KEYDOWN):
            sys.exit()
            
    #screen.fill((0, 80, 0))
    
    #Draw the line
    color = 100, 255, 200
    width = 8
    angle+=theta
    xa=r*math.sin(3*angle)
    ya=r*math.cos(7*angle)
    pygame.draw.line(screen, color, (x, y), (x+xa, y+ya), width)
    x=x+xa
    y=y+ya
    
    pygame.display.update()
