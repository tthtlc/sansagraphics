import sys
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print('Error: PyOpenGL not installed properly')
  sys.exit(  )

import array
import signal

def signal_handler(signal, frame):
        print('u pressed ctrl-c')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
###signal.pause()

fullscreen = False
mouseDown = False

xrot = 0.0
yrot = 0.0

xdiff = 0.0
ydiff = 0.0

def drawBox():
	glBegin(GL_QUADS)

	glColor3f(1.0, 0.0, 0.0)
	## FRONT
	glVertex3f(-0.5, -0.5, 0.5)
	glVertex3f( 0.5, -0.5, 0.5)
	glVertex3f( 0.5, 0.5, 0.5)
	glVertex3f(-0.5, 0.5, 0.5)
	## BACK
	glVertex3f(-0.5, -0.5, -0.5)
	glVertex3f(-0.5, 0.5, -0.5)
	glVertex3f( 0.5, 0.5, -0.5)
	glVertex3f( 0.5, -0.5, -0.5)

	glColor3f(0.0, 1.0, 0.0)
	## LEFT
	glVertex3f(-0.5, -0.5, 0.5)
	glVertex3f(-0.5, 0.5, 0.5)
	glVertex3f(-0.5, 0.5, -0.5)
	glVertex3f(-0.5, -0.5, -0.5)
	## RIGHT
	glVertex3f( 0.5, -0.5, -0.5)
	glVertex3f( 0.5, 0.5, -0.5)
	glVertex3f( 0.5, 0.5, 0.5)
	glVertex3f( 0.5, -0.5, 0.5)

	glColor3f(0.0, 0.0, 1.0)
	## TOP
	glVertex3f(-0.5, 0.5, 0.5)
	glVertex3f( 0.5, 0.5, 0.5)
	glVertex3f( 0.5, 0.5, -0.5)
	glVertex3f(-0.5, 0.5, -0.5)
	## BOTTOM
	glVertex3f(-0.5, -0.5, 0.5)
	glVertex3f(-0.5, -0.5, -0.5)
	glVertex3f( 0.5, -0.5, -0.5)
	glVertex3f( 0.5, -0.5, 0.5)
	glEnd()


def init():
	glClearColor(0.93, 0.93, 0.93, 0.0)

	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glClearDepth(1.0)

	return True


def display():
	global xrot, yrot
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	gluLookAt(
		0.0, 0.0, 3.0,
		0.0, 0.0, 0.0,
		0.0, 1.0, 0.0)

	glRotatef(xrot, 1.0, 0.0, 0.0)
	glRotatef(yrot, 0.0, 1.0, 0.0)

	drawBox()

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

	glutCreateWindow("13 - Solid Shapes")

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
