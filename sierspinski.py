
### http://www.de-brauwer.be/wiki/wikka.php?wakka=PyOpenGLSierpinski

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random

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

    x=[0.0,640.0,320.0]
    y=[0.0,0.0  ,480.0]
    z=[0.0,0.0  ,0.0]

    curx=0
    cury=320
    curz=0
    glVertex3f(curx,cury,curz)
    for i in range(0,500000):
        idx=random.randint(0,2)
        curx=(curx+x[idx])/2.0
        cury=(cury+y[idx])/2.0
        curz=(curz+z[idx])/2.0
        glVertex3f(curx,cury,curz)
    glEnd()
    glFlush()

def display(  ):
	glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
	glMatrixMode( GL_PROJECTION )
	glLoadIdentity( )
	glOrtho( -2, 2, -2, 2, -2, 2 )
	glMatrixMode( GL_MODELVIEW )
	glLoadIdentity( )
	glRotatef( animationAngle, 1, 1, 1 )
	glEnableClientState( GL_COLOR_ARRAY )
	glEnableClientState( GL_VERTEX_ARRAY )
	glVertexPointer( 3, GL_FLOAT, 0, vertices.tostring( ) )
	glDrawElements( GL_QUADS, 24, GL_UNSIGNED_BYTE, cIndices.tostring( ) )
	glColorPointer( 3, GL_FLOAT, 0, colors.tostring( ) )
	glDisableClientState( GL_COLOR_ARRAY )
	glDisableClientState( GL_VERTEX_ARRAY )
	glutSwapBuffers( )

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow("Sierpinski")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()

