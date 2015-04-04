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

moving_angle=math.pi/30
delta = 0.0

while not done:

    t=t+1
    
    # for fun comment out these two lines

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # Get a perspective at the helix

    glMatrixMode(GL_PROJECTION);    

    glLoadIdentity()
    gluPerspective(90,1,0.01,1000)
    gluLookAt(sin(t/200.0)*3,sin(t/500.0)*3,cos(t/200.0)*3,0,0,0,0,1,0)

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

    #pulse = sin(t/30)*0.5+0.5 # try this one
    pulse = 0

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

    glBegin(GL_TRIANGLE_STRIP);
    #pulse2 = 0.5
    round = 4
    ngon = 90
    theta=2*math.pi/ngon
    theta1=0.0
    phi1=0.0

    for i in range(0,round*ngon):

	#pulse2 += 0.5
        #if (i%2==0):
        #    glTexCoord2f(0,i);
        #    glVertex3f( cos(i/r), -2.5+i*0.05, sin(i/r));            
#            glVertex3f( cos(i/r)*pulse2, -2.5+i*0.05, sin(i/r)*pulse2);
        #else:
        #glTexCoord2f(1,i);
	## orig
        ##glVertex3f( cos(i*theta), sin(i*theta*4)-cos(i*theta*3), sin(i*theta));
	theta1 += theta
	phi1 = 2*math.pi - 2*theta1
	delta += moving_angle
	ry = cos(theta1 + delta)
	rx = sin(theta1 + delta)*cos(phi1 + delta)
	rz = sin(theta1 + delta)*sin(phi1 + delta)
	rx1 = sin(phi1+delta)*cos(theta1+delta)
	ry1 = cos(theta1+delta)+sin(phi1+delta)

        #glVertex3f( cos(i/r)*pulse2, -2.5+i*0.05, sin(i/r)*pulse2);
        #glVertex3f( cos(i*theta), sin(i*theta)+cos(i*theta), sin(i*theta));            
#            glVertex3f( cos(i/r+3.14)*pulse2, -2.5+i*0.05+d+pulse2*1, sin(i/r+3.14)*pulse2);
	if (i==0):
		sx=rx
		sy=ry
		sz=rz
		sx1=rx1
		sy1=ry1
		sz1=rz
		
        glVertex3f( rx, ry, rz)
        glVertex3f( rx1, ry1, rz)

    #glVertex3f( sx, sy, sz)
    #glVertex3f( sx1, sy1, sz1)
    glEnd();
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

    glFlush()
    #glutSwapBuffers()
    #glFlush()
    glDeleteTextures(texture)
    pygame.display.flip()
