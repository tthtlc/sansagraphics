# Recursively draw the Mandelbrot set
# Dependencies: Python 2.7.5, PyGame 1.9.1

import pygame
import math
import cmath
from pygame.locals import QUIT
from sys import exit
import sys, os

from OpenGL.GL import *
from OpenGL.GLU import *

# size must be a power of 2 or you will get rounding errors in the image
# E.g. 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, ...
size = 512

pygame.init()
surface = pygame.display.set_mode((size, size), 0, 32)

# Mandelbrot drawing area
xa = -2.0
xb = 2.0
ya = -1.5
yb = 1.5
mouseDown = True

# maximum iterations
maxIt = 256

def pump():
    # pump the event queue so the window is responsive, exit if signaled
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

def point(x, y):
    global xa, ya, xb, yb, size
    # get the escape value of a specific coordinate in the Mandelbrot set
    h = 0.05
    x1 = y * (yb - ya) / size  + ya
    y1 = x * (xb - xa) / size  + xa
    z = x1 + y1 * 1j
    #c = 0.56667 - 0.5 * 1j
    #x1 = 0.001
    #y1 = 0.001
    for i in xrange(maxIt):
    	z = x1 + y1 * 1j
        myabs = abs(z)
        if myabs > 1.5: break
        elif myabs > 2.0: break
        elif myabs > 2.5: break
        elif myabs > 3.0: break
	x2 = x1 - h * math.sin(y1 + math.tan(3*y1))
	y2 = y1 - h * math.sin(x1 + math.tan(3*x1))
	x1 = x2
	y1 = y2
    return i

def col(c):
    # return a color variable computed from a escape value
    return (c % 4 * 64, c % 8 * 32, c % 16 * 16)
    ##return ((((c % 16) * 16) + c % 8 * 32)%256 , c % 8 * 32 , (((256-c) % 16) * 16))

def mandel(x, y, i_size):
    global surface
    p1 = point(x, y)
    half = i_size / 2
    # if half > 1 then there are still possible sub-divisions
    if half > 1:
        # if all the pixels around the square are the same then it can just
        # be filled instead of sub-divided - test the square
        test = False
        for i in xrange(i_size):
            t1 = point(x, y + i)
            t2 = point(x + i, y)
            t3 = point(x + i_size, y + i)
            t4 = point(x + i, y + i_size)
            if (p1 != t1 or p1 != t2 or p1 !=t3 or p1 != t4):
                test = True
                break
        if test:
            # The colors all around the square are not equal so sub-divide
            mandel(x, y, half)
            mandel(x + half, y, half)
            mandel(x + half, y + half, half)
            mandel(x, y + half, half)
        else:
            # This is a base case, all square border points are same color
            # fill area and return back up the stack
            surface.fill(col(p1), (x, y, i_size, i_size))
    else:
        # This is a base case, a 2x2 block. Plot the four pixels
        # and return back up the stack
        p2 = point(x + i_size - 1, y)
        p3 = point(x + i_size - 1, y + i_size - 1)
        p4 = point(x, y + i_size - 1)
        surface.lock()
        surface.set_at((x, y), col(p1))
        surface.set_at((x + i_size - 1, y), col(p2))
        surface.set_at((x + i_size - 1, y + i_size - 1), col(p3))
        surface.set_at((x, y + i_size - 1), col(p4))
        surface.unlock()

    pygame.display.update()
    pump()

def GetInput():
    global mouseDown, xa, xb, ya, yb, size
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:####or key[K_ESCAPE]:
		pygame.quit()	
		sys.exit()
	elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
		x,y = event.pos
		mouseDown = True
    		surface.fill(col(0), (0, 0, size, size))

		new_xa=xa+x*(xb-xa)/size/1.0-(xb-xa)/8.0
		new_xb=xa+x*(xb-xa)/size/1.0+(xb-xa)/8.0
		new_ya=ya+y*(yb-ya)/size/1.0-(yb-ya)/8.0
		new_yb=ya+y*(yb-ya)/size/1.0+(yb-ya)/8.0

		xa = new_xa
		xb = new_xb
		ya = new_ya
		yb = new_yb
		print x,y, size
		print xa, xb, ya, yb
# calculate the image

# Wait for user to click close widget on window

def InitScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION);    

    glLoadIdentity()
    gluPerspective(90,1,0.01,1000)
    ##gluLookAt(sin(t/200.0)*3,sin(t/500.0)*3,cos(t/200.0)*3,0,0,0,0,1,0)

    glMatrixMode(GL_MODELVIEW)

    texture=glGenTextures( 1 )

    glBindTexture( GL_TEXTURE_2D, texture );
    glTexEnvf( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE );

    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S,
                     GL_REPEAT);
    glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T,
                     GL_REPEAT );
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

while True:
    GetInput()
    if (mouseDown):
    	#InitScreen()
	mandel(0, 0, size)
	mouseDown = False
