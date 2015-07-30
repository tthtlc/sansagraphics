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
import random

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
#
signal.signal(signal.SIGINT, signal_handler)
###signal.pause()

import math

fullscreen = False
mouseDown = False

xrot = 0.2
yrot = 0.0
zrot = 0.0

xdiff = 0.0
ydiff = 0.0

def col(c):
	# return a color variable computed from a escape value
	return (c % 4 * 64, c % 8 * 32, c % 16 * 16)

def init():
#	glClearColor(0.93, 0.93, 0.93, 0.0)
	glClearColor(1.0,1.0,1.0,0.0)
	glClearColor(0.0, 0.0, 0.0, 1.0)
	glClearColor(0.0, 0.0, 0.0, 0.0)

	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glClearDepth(1.0)

	return True

def DrawEllipsoid(uistacks, uislices, fA, fB, fC):
	global counter
	tstep = 2*math.pi/uislices
	sstep = 2*math.pi/uistacks
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
	#t = -math.pi/2
	for i in range(4*uislices):
		t = tstep*i
		glBegin(GL_TRIANGLE_STRIP)
	#	s = -2*math.pi/2
		vart=4
		myvars=1
		for j in range(uistacks+1):
			s = sstep*j
			x=math.cos(vart*t) * math.cos(vart*t) * math.cos(myvars*t) 
			y=math.cos(vart*t) * math.cos(vart*t) * math.sin(myvars*t) 
			z=math.sin(vart*t) * math.sin(vart*t) 
			glVertex3f(0.0, 0.0,0.0)
			glVertex3f(x,y,z)
			cx = int (x * 256)
			cy = int (y * 256)
			cz = int (z * 256)
			glColor3b(cx % 4 * 64, cy % 8 * 32, cz % 16 * 16)
			
			#glVertex3f(fA * math.cos(vart*t) * math.cos(myvars*s) * math.sin(t), fB * math.cos(vart*t) * math.sin(myvars*s) * math.sin(t), fC * math.sin(vart*t) * math.cos(t))
			#glVertex3f(fA * math.cos(vart*t+tstep) * math.cos(myvars*s)*math.sin(t), fB *math.cos(vart*t+tstep) * math.sin(myvars*s)*math.sin(t), fC * math.sin(vart*t+tstep)*math.cos(t))
		glEnd()


def display():
	global xrot, yrot, zrot
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	gluLookAt(
		0.0, 0.0, 10.0,
		0.0, 0.0, 0.0,
		0.0, 1.0, 0.0)

	glRotatef(xrot, 1.0, 0.0, 0.0)
	glRotatef(yrot, 0.0, 1.0, 0.0)
	glRotatef(zrot, 0.0, 0.0, 1.0)

    	#glutWireCube(1)
 	glColor3f(0.5, 0.0, 1.0)
	#glutWireSphere(4,10,10)
	DrawEllipsoid(30, 120, 1.1, 2.1, 5.1)

	#void glutSolidTorus(GLdouble innerRadius,
        #            GLdouble outerRadius,
        #            GLint nsides, GLint rings);
	#void glutWireTorus(GLdouble innerRadius,
        #           GLdouble outerRadius,
        #          GLint nsides, GLint rings);

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
	global xrot, yrot, zrot
	global mouseDown
	if not (mouseDown):
		xrot += 0.3 
		yrot += 0.3
		zrot += 1.0

	glutPostRedisplay()


#def keyboard(*args):
#	##print args[0]
#	if (args[0]==27):
#	##	print args[0]
#		sys.exit(1)
#

#def specialKeyboard(*args):
#	##print args[0]
#	if (args[0] == GLUT_KEY_F1):
#		fullscreen = not(fullscreen)
#
#		if (fullscreen):
#			glutFullScreen()
#		else:
#			glutReshapeWindow(500, 500)
#			glutPositionWindow(50, 50)
#
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
	glutInitWindowSize(1024, 768)

	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)

	glutCreateWindow("13 - Solid Shapes")

	glutDisplayFunc(display)
	#glutKeyboardFunc(keyboard)
	#glutSpecialFunc(specialKeyboard)
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
