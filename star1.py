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

def star(t,ngon,ngon2, length):
	angle=(ngon+ngon2)*360/ngon
	for i in range(ngon):
		t.forward(length)
		t.right(angle)

p = t.Pen()
p.reset()
p.down()
p.speed(100)
ts = t.getscreen()
ts.colormode(255)

star(t,7,3,100)
t.forward(70)
star(t,5,2,100)
t.forward(70)
star(t,9,4,100)
raw_input()
