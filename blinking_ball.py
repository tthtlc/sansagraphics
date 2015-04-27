# Pygame/PyopenGL example by Bastiaan Zapf, Apr 2009
###   From http://python-opengl-examples.blogspot.sg/
#
# Draw an helix, wiggle it pleasantly
#
# Keywords: Alpha Blending, Textures, Animation, Double Buffer

from OpenGL.GL import *
from OpenGL.GLU import *

from math import * # trigonometry
import math

import pygame # just to get a display

# get an OpenGL surface

xcolor = 0.0
ycolor = 0.0
zcolor = 0.0

pygame.init() 
pygame.display.set_mode((800,600), pygame.OPENGL|pygame.DOUBLEBUF)

# How to catch errors here?

done = 0

t=0

delta = 0.0
ngon = 60

while not done:

    t=t+1
    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION);    
    glLoadIdentity()
    gluPerspective(90,1,0.01,0000)
    gluLookAt(sin(t*2*math.pi/60)*3,sin(t*2*math.pi/60)*3,0,0,0,0,0,1,0)


    # Draw the helix (this ought to be a display list call)

    glMatrixMode(GL_MODELVIEW)

    # get a texture (this ought not to be inside the inner loop)

    texture=glGenTextures( 1 )

    glBindTexture( GL_TEXTURE_2D, texture );
    glTexEnvf( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE );

    # set sane defaults for a plethora of potentially uninitialized
    # variables

    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S,
                     GL_REPEAT);
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,
                     GL_REPEAT );
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    # a texture

    pulse = 0
#    pulse = sin(t/30)*0.5+0.5 # try this one

    texdata=[[[0.0,0,1,1],
              [0.0,0,0,0],
              [0.0,1,0,1],
              [0.0,0,0,0]],
             [[0.0,0,0,0],
              [pulse,pulse,pulse,1],
              [pulse,pulse,pulse,1],
              [0.0,0,0,0]],
             [[0.0,1,0,1],
              [1,pulse,pulse,1],
              [pulse,pulse,0,1],
              [0.0,0,0,0]],
             [[0.0,0,0,0],
              [0.0,0,0,0],
              [0.0,0,0,0],
              [0.0,0,0,0]]];

    glTexImage2Df(GL_TEXTURE_2D, 0,1,0,GL_RGBA,
                  texdata)

    glEnable(GL_BLEND);
    glBlendFunc (GL_SRC_ALPHA, GL_ONE); # XXX Why GL_ONE?
# alternatively:
#   glEnable(GL_DEPTH_TEST);

    #glEnable( GL_TEXTURE_2D );
    # use the texture
    #glBindTexture( GL_TEXTURE_2D, texture );

    # vertices & texture data

    glBegin(GL_LINE_STRIP);
    #pulse2 = 0.5
    round = 4
    phi1=0.0

    theta = 2*math.pi/ngon
    for i in range(0,ngon):
    	phi = 2*math.pi/ngon
	theta1 = theta*i
    	for j in range(0,ngon):
	    phi1 = phi*j
	    ry = cos(theta1 + delta)
	    rx = sin(theta1 + delta)*cos(phi1 + delta)
	    rz = sin(theta1 + delta)*sin(phi1 + delta)

	    if (i==0):
		sx=rx
		sy=ry
		sz=rz
		
            glVertex3f( rx, ry, rz)
            #glVertex3f( rx1, ry1, rz)

    #glVertex3f( sx1, sy1, sz1)
    xcolor += 0.02
    ycolor += 0.03
    zcolor += 0.01

    if xcolor > 1.0:
	xcolor = 0.0
    if ycolor > 1.0:
	ycolor = 0.0
    if zcolor > 1.0:
	zcolor = 0.0

    glColor3f(xcolor, ycolor, zcolor)
    #glColor3f(0.3, 0.4, 0.5)

    glEnd();
    glFlush()
    #glutSwapBuffers()
    #glFlush()
    glDeleteTextures(texture)
    pygame.display.flip()
    delta += 2*math.pi / 30
