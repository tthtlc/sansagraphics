
# Drawing Lines

import sys
import math
import pygame
import random
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)

pygame.init()


screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Rotating Lines")

PI = 3.141592653
i=0
x=100
y=100

xa=0
ya=0
n=60
theta=2*PI/n
angle=0.0
xtranslate=300
ytranslate=250
radius=200
coord=[(0,0)]*n
for nn in range(n):
    angle=nn*theta
    xa=radius*math.sin(angle) + xtranslate
    ya=radius*math.cos(angle) + ytranslate
    coord[nn]=(xa,ya)

#    for even in pygame.event.get():
#        if even.type in (QUIT, KEYDOWN):
#            sys.exit()
            

while 2>1:
    #screen.fill((0, 80, 0))
    
    #Draw the line
    color = 100, 255, 200
    width = 1
    random_jump=random.randint(2,6)
    for circle_num in range(n):
        opp_num=(circle_num+n/2+random_jump)%n
        #print(circle_num,opp_num)
        #print(coord[circle_num], coord[opp_num])
        pygame.draw.line(screen, color, coord[circle_num%n], coord[opp_num], width)
    
    pygame.display.update()
    raw_input()
    screen.fill(black)
