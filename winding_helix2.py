# Keywords: Alpha Blending, Textures, Animation, Double Buffer
# most basic winding:   just a shift of math.pi away from one another
# compare with surface_linev2.py
# notice that this present does nt differ much from surface_linev22.py

from OpenGL.GL import *
from OpenGL.GLU import *

from math import * # trigonometry
import math

import pygame # just to get a display

# get an OpenGL surface

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

    round = 90
    ngon = 30
    stepsize=2.0*math.pi/ngon
    stepsize2=2.0*math.pi/round/ngon
    offsetsize=2.0*math.pi/ngon/round
    theta=0.0
    delta=0.0
    R=1.0
    r=0.2

    for j in range(round+1):
        rx = (R + r*cos(theta))*cos(delta)
        rz = (R + r*cos(theta))*sin(delta)
        ry = (r*sin(theta))
        glBegin(GL_LINE_STRIP);
        glVertex3f( rx, ry, rz)
        glColor3f(1.0,1.0,0.0)
        for i in range(ngon):
            theta += stepsize + offsetsize
            delta += stepsize2
    
            rx = (R + r*cos(theta))*cos(delta)
            rz = (R + r*cos(theta))*sin(delta)
            ry = (r*sin(theta))
    
            glVertex3f( rx, ry, rz)

        glEnd();


    glFlush()
    pygame.display.flip()
