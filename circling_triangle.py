#!python3
### https://sites.google.com/site/algorithms2013/home/python-turtle-graphics
# space filling hilbert curve in python 3
# adapted from http://www.fundza.com/algorithmic/space_filling/hilbert/basics/index.html
import sys, math, time
import turtle as t
#try:
#from OpenGL.GLUT import *
#from OpenGL.GL import *
#from OpenGL.GLU import *
#except:
#  print('Error: PyOpenGL not installed properly')
#  sys.exit(  )

import array
import signal
import random

def signal_handler(signal, frame):
        print('u pressed ctrl-c')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

## a=> b-a-b
## b=> a+b+a

mycolor = ['blue', 'DarkOrchid4', 'forest green', 'gold4', 'gray', 'green', 'navy', 'purple', 'red', 'yellow' ]

def triangle(t, length, gap):
	t.forward(length)
	t.left(120)
	t.forward(length)
	t.left(120)
	t.forward(length)
	t.left(120)
	t.left(gap)

xcolor = 0.1
ycolor = 0.2

p = t.Pen()
p.reset()
p.down()
p.speed(100)
ts = t.getscreen()
ts.colormode(255)
length = 50
count = 0

while length < 500:
	n=20
	gap = 360/n
	while n>0:
		triangle(t, length, gap)
		n = n - 1
		t.color(mycolor[count%10])
 		count = count + 1
	length = length + 50
raw_input()
