
# space filling hilbert curve in python 3
# adapted from http://www.fundza.com/algorithmic/space_filling/hilbert/basics/index.html

import sys
import turtle as t
import signal

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except ImportError:
    print('Error: PyOpenGL not installed properly')
    sys.exit()

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

## a => b-a-b
## b => a+b+a

def star(t, depth, ngon, length):
    global xcolor, ycolor, zcolor
    if depth > 0:
        angle = 360 / ngon
        for i in range(ngon):
            t.forward(length)
            star(t, depth - 1, ngon, length / 2)
            t.backward(length)
            t.right(angle)
        xcolor += 1 / depth
        ycolor += 1 / depth
        zcolor += 1 / depth
        glColor3f(xcolor, ycolor, zcolor)

xcolor = 0.1
ycolor = 0.2
zcolor = 0.3

p = t.Turtle()
p.speed(0)
ts = t.getscreen()
ts.colormode(1.0)  # Use color mode in range [0, 1] for OpenGL compatibility

star(p, 4, 5, 100)
t.done()

