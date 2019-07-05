
###
# pip install PyOpenGL
# pip install pygame

from OpenGL.GL import *
from OpenGL.GLU import *

from math import * # trigonometry
import math

import pygame # just to get a display

# get an OpenGL surface
radius_array=[1.0, 0.5, 0.25, 1.0, 0.5, 0.25]
arraylen=len(radius_array)
velocity_rate=0.0
anglesize = 2*math.pi/30

def draw_circle(xcenter, ycenter, recursion):
    global velocity_rate
    ngon = 30
    stepsize=2*math.pi/ngon
    theta=0.0
    radius=radius_array[arraylen-recursion]

    glBegin(GL_LINE_STRIP);
    glColor3f(1.0,1.0,1.0)
    for j in range(ngon+1):
	rx = (xcenter + radius*cos(theta))
	ry = (ycenter + radius*sin(theta))
	theta += stepsize
	glVertex2f( rx, ry )
    glEnd();
    glFlush()
    pygame.display.flip()
    rx = (xcenter + radius*cos(velocity_rate))
    ry = (ycenter + radius*sin(velocity_rate))
    velocity_rate += anglesize
    if (recursion-1>0):
    	draw_circle(rx,ry,recursion-1)

pygame.init() 
pygame.display.set_mode((800,600), pygame.OPENGL|pygame.DOUBLEBUF)

# How to catch errors here?

done = False

t=0

while not done:

    t=t+1
    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # Get a perspective at the helix

    glMatrixMode(GL_PROJECTION);    

    glLoadIdentity()
    gluPerspective(90,1,0.01,1000)
    gluLookAt(sin(t/200.0)*3,sin(t/500.0)*3,cos(t/200.0)*3,0,0,0,0,1,0)

    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_BLEND);
    glBlendFunc (GL_SRC_ALPHA, GL_ONE);
    glEnable( GL_TEXTURE_2D );
    glEnable( GL_COLOR_MATERIAL );

    draw_circle(0.0, 0.0, 6)

