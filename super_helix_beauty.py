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

pygame.init() 
pygame.display.set_mode((800,600), pygame.OPENGL|pygame.DOUBLEBUF)

# How to catch errors here?

def double_rotation(oldy, angle1, angle2):
	
        x=cos(angle1)
	##y=-2.5+i*0.05+d
	y=oldy
	z=sin(angle1)
	newx=x*math.cos(angle2) - y*math.sin(angle2)
	newy=x*math.sin(angle2) + y*math.cos(angle2)
	newz=z
	return [newx, newy, newz]

done = False

t=0

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

    glBegin(GL_LINE_STRIP);
    #pulse2 = 0.5

    r=5.0 # try other values - integers as well
    d=1   # try other values
    rotation=4
    ngon=36
    maxi=rotation*ngon
    maxj=ngon
    theta=2*math.pi/ngon
    phi=2*math.pi/maxj
    shift=math.pi/3
    for i in range(0,maxi):
    	for j in range(0,maxj):
	#pulse2 += 0.5
        #if (i%2==0):
        #    glTexCoord2f(0,i);
        #    glVertex3f( cos(i/r), -2.5+i*0.05, sin(i/r));            
#            glVertex3f( cos(i/r)*pulse2, -2.5+i*0.05, sin(i/r)*pulse2);
        #else:
        #glTexCoord2f(1,i);
######### to do:   
        	[x,y,z]=double_rotation(-2.5+i*0.05+d, i*theta+shift, j*phi)
        	glVertex3f(x,y,z)
        #glVertex3f( cos(i*theta)*pulse2, -2.5+i*0.05, sin(i*theta)*pulse2);
        	[x,y,z]=double_rotation(-2.5+i*0.05+d, i*theta, j*phi)
        	glVertex3f(x,y,z)
        ###glVertex3f( cos(i*theta), -2.5+i*0.05, sin(i*theta));            
#            glVertex3f( cos(i/r+3.14)*pulse2, -2.5+i*0.05+d+pulse2*1, sin(i/r+3.14)*pulse2);
        
    glEnd();

    glFlush()

    glDeleteTextures(texture)
    pygame.display.flip()
