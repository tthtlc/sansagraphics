# Pygame/PyopenGL example by Bastiaan Zapf, Apr 2009
###   From http://python-opengl-examples.blogspot.sg/
#
# Draw an helix, wiggle it pleasantly
#
# Keywords: Alpha Blending, Textures, Animation, Double Buffer

from OpenGL.GL import *
from OpenGL.GLU import *

from math import * # trigonometry

import pygame # just to get a display

# get an OpenGL surface

pygame.init() 
pygame.display.set_mode((800,600), pygame.OPENGL|pygame.DOUBLEBUF)

# How to catch errors here?

done = False

t=600

PI2 = 2*3.141592653
Q=0.2
irange=100
jrange=10
krange=10
kw=krange/PI2
jw=jrange/PI2
iw=irange/PI2

while not done:

    t=t+3
    
    # for fun comment out these two lines

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # Get a perspective at the helix

    glMatrixMode(GL_PROJECTION);    

    glLoadIdentity()
    gluPerspective(90,1,0.01,1000)

    ## this will rotate the angle of view all the time, approximately around the x-z axis
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
#    glEnable(GL_DEPTH_TEST);

    glEnable( GL_TEXTURE_2D );
    # use the texture
    glBindTexture( GL_TEXTURE_2D, texture );

    # vertices & texture data

    glBegin(GL_TRIANGLE_STRIP);
    #pulse2 = 0.5

    r=1.1 # try other values - integers as well
    R=1.5 # try other values - integers as well
    rr=3.0 # try other values - integers as well
    P=5.0
    kw=6*r
    jw=4*r
    d=1   # try other values
	
    for i in range(0,irange):
    	for j in range(0,jrange):
    	#	for j in range(0,25):

			#pulse2 += 0.5
		        if (i%2==0):
#		            glTexCoord2f(0,i);
		            glVertex3f( R*cos(j/jw), R*sin(i/iw), (R*cos(i/iw) + P)+R*sin(j/jw) )
		        else:
#		            glTexCoord2f(i%10,i);
		            glVertex3f( R*cos(j/jw+3.14), R*sin(i/iw+3.14), (R*cos(i/iw+3.14))+R*sin(j/jw+3.14) )

    glEnd();

    glFlush()

    glDeleteTextures(texture)
    pygame.display.flip()
