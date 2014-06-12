

#!/usr/bin/env python
# encoding=utf-8

import sys
from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex(0.25, 0.25, 0.0)
    glVertex(0.75, 0.25, 0.0)
    glVertex(0.75, 0.75, 0.0)
    glVertex(0.25, 0.75, 0.0)
    glEnd()
    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(250, 250)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('hello')
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == '__main__':
    main()



