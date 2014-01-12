
### http://www.de-brauwer.be/wiki/wikka.php?wakka=PyOpenGLSierpinski

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import sys,signal

import time
import random

mouseDown = False

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
###signal.pause()

def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(0.0,0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)
    

xrot=0.0
yrot=0.0

def idle():
        global xrot, yrot
        if not (mouseDown):
                xrot += 0.3
                yrot += 0.4
	time.sleep(1)
        glutPostRedisplay()

def displayFun1():
    glBegin(GL_POINTS)

    x=[0.0,640.0,320.0]
    y=[0.0,0.0  ,480.0]
    z=[0.0,0.0  ,0.0]

    curx=0
    cury=320
    curz=0
    glVertex3f(curx,cury,curz)
    for i in range(0,5000):
        idx=random.randint(0,2)
        curx=(curx+x[idx])/2.0
        cury=(cury+y[idx])/2.0
        curz=(curz+z[idx])/2.0
        glVertex3f(curx,cury,curz)
    glEnd()

def displayFun(  ):
        global xrot, yrot

	glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
	glMatrixMode( GL_PROJECTION )
	glLoadIdentity( )
	glOrtho( -2, 2, -2, 2, -2, 2 )
	#glMatrixMode( GL_MODELVIEW )
	#glLoadIdentity( )
	##glEnableClientState( GL_COLOR_ARRAY )
	##glEnableClientState( GL_VERTEX_ARRAY )
	### glVertexPointer( 3, GL_FLOAT, 0, vertices.tostring( ) )

        gluLookAt(
                0.0, 0.0, 3.0,
                0.0, 0.0, 0.0,
                0.0, 1.0, 0.0)
        glRotatef(xrot, 1.0, 0.0, 0.0)
        glRotatef(yrot, 0.0, 1.0, 0.0)
	displayFun1()

	## glDrawElements( GL_QUADS, 24, GL_UNSIGNED_BYTE, cIndices.tostring( ) )

	## glColorPointer( 3, GL_FLOAT, 0, colors.tostring( ) )
	#glDisableClientState( GL_COLOR_ARRAY )
	#glDisableClientState( GL_VERTEX_ARRAY )

        glFlush()
        glutSwapBuffers()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow("Sierpinski")
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    initFun()
    glutDisplayFunc(displayFun)
    glutIdleFunc(idle)
    glutMainLoop()

