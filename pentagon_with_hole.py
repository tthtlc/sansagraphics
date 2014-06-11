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

signal.signal(signal.SIGINT, signal_handler)
###signal.pause()

import math

def draw_modding_polygon(rc, gc, bc, R1, R2, alpha, beta,theta, inner_ngon, outer_ngon):

	glBegin(GL_TRIANGLE_STRIP)

	myangle = 0.0

        glColor3f(rc, gc, bc)
	angle_step=2*math.pi/inner_ngon
	myangle+=angle_step+1/360*2*math.pi

	for i in range(outer_ngon): 
	    	y = R1*math.sin(myangle+alpha)*math.cos(beta)
	    	x = R2*math.sin(myangle)*math.sin(beta)
	    	z = R2*math.cos(myangle)
	    	glVertex3f(x,y,z)
		myangle+=angle_step
	glEnd()

fullscreen = False
mouseDown = False

xrot = 0.2
yrot = 0.0

xdiff = 0.0
ydiff = 0.0

mycolor=[[0,1,0],[1,0,0],[0,0,1],[0,1,1],[1,1,0],[1,0,1]]

def init():
	glClearColor(0.93, 0.93, 0.93, 0.0)

	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glClearDepth(1.0)

	return True

counter=0
inner_ngon=5

def display():
	global xrot, yrot
	global counter
	global inner_ngon

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	gluLookAt(
		0.0, 0.0, 3.0,
		0.0, 0.0, 0.0,
		0.0, 1.0, 0.0)

	glRotatef(xrot, 1.0, 0.0, 0.0)
	glRotatef(yrot, 0.0, 1.0, 0.0)

	beta=2*math.pi/8
	alpha=2*math.pi/8
	R1=1
	R2=0.8

	[rc,gc,bc]=mycolor[2]

	#### note for below
	#### inner_ngon=5
	#### outer_ngon=7
	#### generally, outer = inner + 2, for smooth transition using TRIANGLE_STRIP drawing
	#### by changing 5 to any number, any ngon with with hole can be implemented.
	outer_ngon=inner_ngon+2
	draw_modding_polygon(rc, gc, bc, R1, R2, 0.0, 0.0,0.0, inner_ngon, outer_ngon)

	glFlush()
	glutSwapBuffers()

    	counter = counter+1
	if counter>100:	
		print "modding..."
		inner_ngon = inner_ngon + 1
    		raw = raw_input()
		counter=0

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




