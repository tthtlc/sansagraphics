import sys
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ''' Error: PyOpenGL not installed properly '''
  sys.exit(  )

import array
import signal

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
###signal.pause()

import math

PI = 3.141592653
ngon=30
angle_step=2*math.pi/ngon
r1_step = 0.05
r2_step = -0.05
delta=0.0
theta1 = 0 ##2*math.pi/3

def draw_ellipse(R1, R2, alpha, beta,theta):
	global delta
	global ngon
	i=0
	angle=0

	glBegin(GL_POLYGON)

        cx=(math.sin((theta-delta)*2)+1)
        cy=(math.sin((alpha-delta)*2-PI/2)+1)
        cz=(math.sin((beta-delta)*2-PI/4)+1)

        glColor3f(cx, cy, cz)

	while i < ngon:
	    y = R1*math.sin(angle+alpha)*math.cos(beta)
	    x = R2*math.sin(angle)*math.sin(beta)
	    z = R2*math.cos(angle)
	    glVertex3f(x,y,z)
	    angle += angle_step
	    i+=1
	glEnd()
	delta += 2*math.pi/60

fullscreen = False
mouseDown = False

xrot = 0.2
yrot = 0.0

xdiff = 0.0
ydiff = 0.0
ndisc = 20

def init():
	glClearColor(0.93, 0.93, 0.93, 0.0)

	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glClearDepth(1.0)

	return True


def display():
	global xrot, yrot
	global ndisc
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	gluLookAt(
		0.0, 0.0, 3.0,
		0.0, 0.0, 0.0,
		0.0, 1.0, 0.0)

	glRotatef(xrot, 1.0, 0.0, 0.0)
	glRotatef(yrot, 0.0, 1.0, 0.0)

	beta=2*PI/8
	alpha=2*PI/8
	R1=1
	R2=0.8
	theta=2*math.pi/30

	for i in range(ndisc):
		#R1 += r1_step
		#R2 += r2_step
		alpha += angle_step
		beta += angle_step
		theta += theta1
		draw_ellipse(R1, R2, alpha, beta, theta)

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
