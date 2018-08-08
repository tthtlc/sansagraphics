import sys
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ''' Error: PyOpenGL not installed properly '''
  sys.exit(0)

import array
import signal
import random

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
###signal.pause()

import math

PI = 3.141592653
ngon=120
angle_step=2*PI/ngon
r1_step = 0.005
r2_step = 0.001
delta=0.6
theta1 = 2*PI/ngon

fullscreen = False
mouseDown = False

xrot = math.pi/30
yrot = math.pi/8

xdiff = 0.0
ydiff = 0.0
ndisc = 20

def init():
#	glClearColor(0.93, 0.93, 0.93, 0.0)
	glClearColor(1.0,1.0,1.0,0.0)
	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClearColor(0.0, 0.0, 0.0, 0.0)

	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glClearDepth(1.0)

	return True

xcolor=0.0
ycolor=0.0
zcolor=0.0

def display():
	global xrot, yrot
	global ndisc
	global xcolor, ycolor, zcolor
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	gluLookAt(
		0.0, 0.0, 10.0,
		0.0, 0.0, 0.0,
		0.0, 1.0, 0.0)

	for i in range(30):
		glRotatef(xrot, 1.0, 0.0, 0.0)
		glRotatef(yrot, 0.0, 1.0, 0.0)
		glutWireTetrahedron(1)

	glRotatef(xrot, 1.0, 0.0, 0.0)
	glRotatef(yrot, 0.0, 1.0, 0.0)
	glutWireTetrahedron(1)

	xcolor += 0.02
	ycolor += 0.03
	zcolor += 0.01
	if xcolor > 1.0:
		xcolor = 0.0
	if ycolor > 1.0:
		ycolor = 0.0
	if zcolor > 1.0:
		zcolor = 0.0
 	glColor3f(xcolor, ycolor, zcolor)
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
	global xrot, yrot, total_count
	global mouseDown
	if not (mouseDown):
		xrot += 0.3
		yrot += 0.4
	total_count += 1
	if (total_count>int(sys.argv[1])):
		sys.exit(0)

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
	global total_count
	glutInit(sys.argv)
	glutInitWindowPosition(50, 50)
	glutInitWindowSize(500, 500)

	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)

	glutCreateWindow("13 - Solid Shapes")

	glutDisplayFunc(display)
	glutKeyboardFunc(keyboard)
	glutSpecialFunc(specialKeyboard)
	glutMouseFunc(mouse)
	glutMotionFunc(mouseMotion)
	glutReshapeFunc(resize)
	if not (init()):
		return 1
	total_count=0
	glutIdleFunc(idle)

	glutMainLoop()

	return 0

if __name__ == "__main__":
    main()
