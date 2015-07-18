#!python3
### https://sites.google.com/site/algorithms2013/home/python-turtle-graphics
# space filling hilbert curve in python 3
# adapted from http://www.fundza.com/algorithmic/space_filling/hilbert/basics/index.html
import sys, math, time
import turtle as t
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ''' Error: PyOpenGL not installed properly '''
  sys.exit(  )

import array
import signal
import random

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

## a=> b-a-b
## b=> a+b+a

def star(t, depth, ngon,length):
    global xcolor, ycolor, zcolor
    if (depth>1):
	angle=360/ngon
	for i in range(ngon):
		t.forward(length)
		star(t,depth-1,ngon,length/2)
		t.forward(-length)
		t.right(angle)
    xcolor += xcolor+1/depth
    ycolor += ycolor+1/depth
    zcolor += zcolor+1/depth
    glColor3f(xcolor+1/depth, ycolor+1/depth, zcolor+1/depth)


xcolor = 0.1
ycolor = 0.2
zcolor = 0.3

p = t.Pen()
p.reset()
p.down()
p.speed(22)
ts = t.getscreen()
ts.colormode(255)

star(t,4,5,100)
raw_input()
