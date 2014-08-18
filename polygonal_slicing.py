### originally from dancing_quad_spiral.py

import sys
from mysansagraphic import *

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ''' Error: PyOpenGL not installed properly '''
  sys.exit(  )

import array
import math
import signal
import random


def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
###signal.pause()

import math

turns1 = 30
turns2 = 3
count=0

fullscreen = False
mouseDown = False

xrot = 0.2
yrot = 0.0

xdiff = 0.0
ydiff = 0.0

def init():
	glClearColor(1.0,1.0,1.0,0.0)
	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClearColor(0.0, 0.0, 0.0, 0.0)

	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glClearDepth(1.0)

	return True

import sys
import OpenGL.GL as gl
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

Vertices = ((-1,-1,-1), (1,-1,-1),
            (1,1,-1), (-1,1,-1),
            (-1,-1,1), (1,-1,1),
            (1,1,1), (-1,1,1))

Colors   = ((0.2,0.5,0.9), (1,0,0),
            (1,1,0), (0,1,0),
            (0,0,1), (1,0,1),
            (1,1,1), (0,1,1))


def my2d_surface(radius1, radius2, turns1, turns2):

    glBlendFunc(GL_SRC_ALPHA_SATURATE, GL_ONE)
    glEnable(GL_BLEND)

    itheta=2*math.pi/turns1
    jtheta=2*math.pi/turns2
    xshift=2*math.pi/4
    yshift=2*math.pi/4
    zshift=2*math.pi/4

    for i in range(0,turns1):
        glBegin(GL_LINE_STRIP)
    	for j in range(0,turns2):
		if j==0:
			rx=radius1*math.cos(j*jtheta)
			ry=radius2*math.sin(i*itheta)
			rz=radius1*math.cos(i*itheta)+radius2*math.sin(j*jtheta)
		if (j%2==0):
			glVertex3f( radius1*math.cos(j*jtheta), radius2*math.sin(i*itheta), (radius1*math.cos(i*itheta))+radius2*math.sin(j*jtheta) )
		else:
			glVertex3f( radius1*math.cos(j*jtheta+xshift), radius2*math.sin(i*itheta+yshift), (radius1*math.cos(i*itheta+zshift))+radius2*math.sin(j*jtheta+zshift) )
                glColor3fv(Colors[i%8])
	glVertex3f( rx, ry, rz )
    	glEnd()

    return 

def display():
	global xrot, yrot
	global turns1, turns2, count

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	gluLookAt(
		0.0, 0.0, 10.0,
		0.0, 0.0, 0.0,
		0.0, 1.0, 0.0)

	glRotatef(xrot, 1.0, 0.0, 0.0)
	glRotatef(yrot, 0.0, 1.0, 0.0)

 	glColor3f(0.5, 0.0, 1.0)

	if count>60:
		count=0
		turns1 = random.randint(20,30)
		turns2 = random.randint(3,6)
		print turns1, turns2
	count = count + 1
	my2d_surface(2.0, 2.0, turns1, turns2)

    	glFlush()
    	glutSwapBuffers()

def resize(*args):
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	glViewport(0, 0, args[0], args[1])

	gluPerspective(45.0, 1.0 * args[0] / args[0], 1.0, 100.0)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()


def idle():
	global xrot, yrot
	global mouseDown
	if not (mouseDown):
		xrot += 0.3
		yrot += 0.4

	glutPostRedisplay()


def keyboard(*args):
	##print args[0]
	if (args[0]==27):
	##	print args[0]
		sys.exit(1)


def specialKeyboard(*args):
	##print args[0]
	if (args[0] == GLUT_KEY_F1):
		fullscreen = not(fullscreen)

		if (fullscreen):
			glutFullScreen()
		else:
			glutReshapeWindow(500, 500)
			glutPositionWindow(50, 50)

def mouse(*args):
	global xrot, yrot
	global xdiff, ydiff
	global mouseDown
	if (args[0] == GLUT_LEFT_BUTTON and args[1] == GLUT_DOWN):
		mouseDown = True
		xdiff = args[2] - yrot
		ydiff = -args[3] + xrot
	else:
		mouseDown = False


def mouseMotion(*args):
	global xrot, yrot
	global xdiff, ydiff
	global mouseDown
	if (mouseDown):
		yrot = args[0] - xdiff
		xrot = args[1] + ydiff
	glutPostRedisplay()


def main():
	glutInit(sys.argv)
	glutInitWindowPosition(50, 50)
	glutInitWindowSize(500, 500)

	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)

	glutCreateWindow("Polyhedral Surface")

	glutDisplayFunc(display)
	glutKeyboardFunc(keyboard)
	glutSpecialFunc(specialKeyboard)
	glutMouseFunc(mouse)
	glutMotionFunc(mouseMotion)
	glutReshapeFunc(resize)

	if not (init()):
		return 1

	glutIdleFunc(idle)

	glutMainLoop()

	return 0

if __name__ == "__main__":
    main()
