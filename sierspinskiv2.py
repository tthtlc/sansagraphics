
### http://www.de-brauwer.be/wiki/wikka.php?wakka=PyOpenGLSierpinski

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
import signal

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
###signal.pause()

def keyPressed(*args):
        # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
            glutDestroyWindow(window)
            sys.exit()

def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(0.0,0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)
    

def displayFun():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)

    x=[0.0,640.0,320.0,160.0]
    y=[0.0,0.0  ,480.0,240.0]

    curx=0
    cury=320.0
    glVertex2f(curx,cury)
    # Monte Carlo method of generating the points
    for i in range(0,500000):
        idx=random.randint(0,3)  
	## the following is a tree method
	## previous curx and cury will determine future values, shifted by 
	## one of 3 method:    0=>no change, 1=>to the right by 640/2 and then
	## to about 45degree=>by 320/2 and 480/2.
        curx=(curx+x[idx])/2.0
        cury=(cury+y[idx])/2.0
        glVertex2f(curx,cury)
    glEnd()
    glFlush()


if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640,480)
    window=glutCreateWindow("Sierpinski")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    glutKeyboardFunc(keyPressed)
    initFun()
    glutMainLoop()

