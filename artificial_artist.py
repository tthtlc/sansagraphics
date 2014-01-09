
# Drawing Lines

import sys
import random
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
XLIMIT=600
YLIMIT=500

delta=0.0
xa=0
ya=0
n=50
theta=2*PI/n
angle=0.0
r=3
while True:
    for even in pygame.event.get():
        if even.type in (QUIT, KEYDOWN):
            sys.exit()
            
    #screen.fill((0, 80, 0))
    
    #Draw the line
    color = 100, 255, 200
    width = 8
    angle+=random.randint(0, 50)*theta
    xa=r*math.sin(angle)
    ya=r*math.cos(angle)

    while ((x+xa)>XLIMIT) or ((x+xa)<0):
    	angle+=random.randint(0, 50)*theta
    	xa=r*math.sin(angle)
    while ((y+ya)>YLIMIT) or ((y+ya)<0):
    	angle+=random.randint(0, 50)*theta
    	ya=r*math.cos(angle)

    delta+=theta
    cx=int(120*(math.sin((delta)/10)+1)+10)
    cy=int(120*(math.sin((delta)*6/10)+1)+10)
    cz=int(120*(math.sin((delta)/10-PI)+1)+10)

    pygame.draw.line(screen, [cx,cy,cz], (x, y), (x+xa, y+ya), width)
    x=x+xa
    y=y+ya
    
    pygame.display.update()
