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
import random

import pygame # just to get a display

# get an OpenGL surface

pygame.init() 
pygame.display.set_mode((800,600), pygame.OPENGL|pygame.DOUBLEBUF)

# How to catch errors here?

done = False
count = 0
mycount = random.randint(2,16)

t=0

Colors   = ((0.2,0.5,0.9), (1,0,0),
            (1,1,0), (0,1,0),
            (0,0,1), (1,0,1),
            (1,1,1), (0,1,1))

while not done:

    t=t+3
    
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

    glTexImage2Df(GL_TEXTURE_2D, 0,4,0,GL_RGBA,
                  texdata)

    glEnable(GL_BLEND);
    glBlendFunc (GL_SRC_ALPHA, GL_ONE); # XXX Why GL_ONE?
# alternatively:
    #glEnable(GL_DEPTH_TEST);

    glEnable( GL_TEXTURE_2D );
    # use the texture
    glBindTexture( GL_TEXTURE_2D, texture );

    # vertices & texture data

    glBegin(GL_TRIANGLE_STRIP);
    #pulse2 = 0.5
    long_ngon = 30
    lat_ngon = 20
    theta_delta=2*math.pi/long_ngon
    phi_delta=math.pi/lat_ngon
    theta=0.0
    phi=0.0
    m0 = 2
    m1 = 1
    m2 = 2
    m3 = 1
    m4 = 2
    m5 = 1
    m6 = 2
    m7 = 1
    
    count += 1
    if count > 10000:
    	mycount = random.randint(1,16)
	count = 0

    for i in range(0,long_ngon):
	theta += theta_delta
    	for j in range(0,lat_ngon):

		#pulse2 += 0.5
	        #if (i%2==0):
	        #    glTexCoord2f(0,i);
	        #    glVertex3f( cos(i/r), -2.5+i*0.05, sin(i/r));            
	#            glVertex3f( cos(i/r)*pulse2, -2.5+i*0.05, sin(i/r)*pulse2);
	        #else:
	        #glTexCoord2f(1,i);
		## orig
	        ##glVertex3f( cos(i*theta), sin(i*theta*4)-cos(i*theta*3), sin(i*theta));
		phi += phi_delta
	
		R = math.sin(m0*phi)**m1 + math.cos(m2*phi)**m3 + math.sin(m4*theta)**m5 + math.cos(m6*theta)**m7
		ry = R*cos(phi)
		rx = R*sin(phi)*cos(theta)
		rz = R*sin(phi)*sin(theta)
	
	        glVertex3f( rx, ry, rz)
	
	glEnd();
	
	glFlush()

    glDeleteTextures(texture)
    pygame.display.flip()
