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

import math
xrot = 0.2
yrot = 0.0

xdiff = 0.0
ydiff = 0.0

### theta is rotation about the z-axis
def draw_ellipse_z(R1, R2, theta, xoffset, yoffset, zoffset):
	angle=0
	ngon=30
	angle_step=2*math.pi/ngon

	glBegin(GL_LINE_STRIP)

        cx=(math.sin(theta))
        cy=(math.cos(theta))
        cz=(math.sin(theta))

        glColor3f(cx, cy, cz)

	### angle is the angle of rotation about the tilted x-z plane, which is again rotated about the z-axis with theta
	for i in range(ngon+1):
	    x = xoffset+R2*math.cos(angle)*math.cos(theta)
	    z = zoffset+R1*math.sin(angle)
	    y = yoffset+R2*math.cos(angle)*math.sin(theta)
	    glVertex3f(x,y,z)
	    angle += angle_step
	glEnd()

fullscreen = False
mouseDown = False

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
		5.0, 5.0, 5.0,
		0.0, 0.0, 0.0,
		0.0, 1.0, 0.0)

	glRotatef(xrot, 1.0, 0.0, 0.0)
	glRotatef(yrot, 0.0, 1.0, 0.0)

	R1=0.8
	R2=0.6
	R3=1.0
	ngon=8
	theta_step=2*math.pi/ngon
	theta=0.0

	for i in range(ngon):

		xoffset=R3*math.cos(theta)
		yoffset=R3*math.sin(theta)
		zoffset=0.0
		draw_ellipse_z(R1, R2, theta, xoffset, yoffset, zoffset)
		theta += theta_step

	### note that the flush/Swp must be outside the glBegin/glEnd() eternal loop.
	### only do it ONCE per display() is called.

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
		xrot += 0.8
		yrot += 0.8

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

	glutCreateWindow("Rotating Ellipse Plane")

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
