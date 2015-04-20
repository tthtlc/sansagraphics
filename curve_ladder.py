### originally from crown_circling.py

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

xrotspiral = 1.0
zrotspiral = 1.0

PI = 3.141592653
ngon=120
angle_step=2*PI/ngon
r1_step = 0.005
r2_step = 0.001
delta=0.6
theta1 = 2*PI/ngon

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

n=1

def circling_on_sphere(circle_radius, sphere_radius, turns):

    global n

    glBlendFunc(GL_SRC_ALPHA_SATURATE, GL_ONE)
    glEnable(GL_BLEND)

    glBegin(GL_LINES)

    ngon=10
    theta1=2*math.pi/ngon
    sphere_gon=5
    yrotate1=360.0/turns
    theta=0.0
    y_rotate_angle=0.0

    for i in range(0,turns):
	for i in range(0,ngon):
		## phi = wrt y axis (sinusoidal, between 45 deg and 135 deg)
		## theta = wrt x axis, on the zx plane (normal increment)
		#phi1=math.pi*math.sin(ngon*theta)/4
		#phi=math.pi/2 - phi1
		cx=(circle_radius*(1+0.5*math.cos(10*theta)))*math.sin(theta)
		cy=(circle_radius*(1+0.5*math.cos(10*theta)))*math.cos(theta*n)
		cz=sphere_radius
		(rx,ry,rz)=point_rotatey(cx,cy,cz, y_rotate_angle)
		#rx=radius*math.sin(phi)*math.cos(theta)
		#rz=radius*math.sin(phi)*math.sin(theta)
		#ry=radius*math.cos(phi)
	
		if (i==0):
			rx0=rx
			ry0=ry
			rz0=rz
		if (i==1):
			rx1=rx
			ry1=ry
			rz1=rz
	
	        glVertex3f( rx, ry, rz )
	    	glColor3fv(Colors[i%8])
	        #glVertex3f( rx, ry, rz )
		theta += theta1
	y_rotate_angle += yrotate1
    #glVertex3f( rx0, ry0, rz0 )
    #glVertex3f( rx1, ry1, rz1 )

    glEnd()
    return 

def display():
	global xrot, yrot
	global xrotspiral, zrotspiral

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	gluLookAt(
		0.0, 0.0, 10.0,
		0.0, 0.0, 0.0,
		0.0, 1.0, 0.0)

	glRotatef(xrot, 1.0, 0.0, 0.0)
	glRotatef(yrot, 0.0, 1.0, 0.0)

 	glColor3f(0.5, 0.0, 1.0)

	circling_on_sphere(1.0, 2.0, 60)

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
	global n
	
	if not (mouseDown):
		xrot += 0.3
		yrot += 0.4
	else:
		n = n+1

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
    print 'Please click the mouse:   LHS'
    main()
