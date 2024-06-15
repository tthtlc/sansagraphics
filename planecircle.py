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
import random

def signal_handler(signal, frame):
        print('u pressed ctrl-c')
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

xrot = 0.2
yrot = 0.0

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

Colors   = ((0,0,0), (1,0,0),
            (1,1,0), (0,1,0),
            (0,0,1), (1,0,1),
            (1,1,1), (0,1,1))

def planespiral(radius,ngon,turn):
        theta = 2 * math.pi / ngon
	vertices=[]
	rad1=radius/turn/ngon
	rad=0.0
	for i in range(ngon*turn):
		x = rad * math.cos(i*theta)
		z = rad * math.sin(i*theta)
		y = 0.0
        	vertices.append((x,y,z))
		rad += rad1
	return vertices

def planecircle(radius,ngon):
        theta = 2 * math.pi / ngon
	vertices=[]
	for i in range(ngon):
		x = radius * math.cos(i*theta)
		z = radius * math.sin(i*theta)
		y = 0.0
        	vertices.append((x,y,z))
	x=radius
	z=0.0
        vertices.append((x,y,z))
	return vertices

def rotate_theta_alpha(vertices, theta, alpha):
	new_vertices=[]
        for v in range(len(vertices)):
		(x,y,z) = vertices[v]
		x *= math.sin(theta) * math.cos(alpha)
		y *= math.cos(theta)
		z *= math.sin(theta) * math.sin(alpha)
        	new_vertices.append((x,y,z))
	return new_vertices

def point_rotatex(x,y,z, angle):
	rad = angle * math.pi / 180
	cosa = math.cos(rad)
	sina = math.sin(rad)
	y = y * cosa - z * sina
	z = y * sina + z * cosa
	return (x,y,z)

def plane_rotatex(vertices, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
	new_vertices=[]
	for i in range(len(vertices)):
		(x,y,z) = vertices[i]
		(x,y,z)=point_rotatex(x,y,z,angle)	
		new_vertices.append((x,y,z))
	return new_vertices

def point_rotatey(x,y,z, angle):
	rad = angle * math.pi / 180
	cosa = math.cos(rad)
	sina = math.sin(rad)
	z = z * cosa - x * sina
	x = z * sina + x * cosa
	return (x,y,z)
 
def plane_rotatey(vertices, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
	new_vertices=[]
	for i in range(len(vertices)):
		(x,y,z) = vertices[i]
		(x,y,z)=point_rotatey(x,y,z,angle)	
		new_vertices.append((x,y,z))
	return new_vertices

def point_rotatez(x,y,z,angle):
	rad = angle * math.pi / 180
	cosa = math.cos(rad)
        sina = math.sin(rad)
        x = x * cosa - y * sina
        y = x * sina + y * cosa
	return (x,y,z)
 
def plane_rotatez(vertices, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
	new_vertices=[]
	for i in range(len(vertices)):
		(x,y,z) = vertices[i]
		(x,y,z)=point_rotatez(x,y,z,angle)	
		new_vertices.append([x,y,z])
	return new_vertices

def face(a,b,c,d):
    '''draw a face defined by four vertex indices'''
    glBegin(GL_QUADS)
    glColor3fv(Colors[a]);    glVertex3fv(Vertices[a]);
    glColor3fv(Colors[b]);    glVertex3fv(Vertices[b]);
    glColor3fv(Colors[c]);    glVertex3fv(Vertices[c]);
    glColor3fv(Colors[d]);    glVertex3fv(Vertices[d]);
    glEnd()

def colorcube():
    '''Draws the entire cube, six faces'''
    face(0,3,2,1)
    face(2,3,7,6)
    face(0,4,7,3)
    face(1,2,6,5)
    face(4,5,6,7)
    face(0,1,5,4)

def edge(A, B):
    '''Sends two vertices down the pipeline.  Presumably they form an edge'''
    glVertex3fv(Vertices[A]);
    glVertex3fv(Vertices[B]);

def wireCube():
    glBegin(GL_LINES)
    ## back
    edge(0,1)
    edge(1,2)
    edge(2,3)
    edge(3,0)
    ## front
    edge(4,5)
    edge(5,6)
    edge(6,7)
    edge(7,4)
    ## sides
    edge(0,4)
    edge(1,5)
    edge(2,6)
    edge(3,7)
    glEnd()

def display():
	global xrot, yrot
	global ndisc
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	gluLookAt(
		0.0, 0.0, 10.0,
		0.0, 0.0, 0.0,
		0.0, 1.0, 0.0)

	glRotatef(xrot, 1.0, 0.0, 0.0)
	glRotatef(yrot, 0.0, 1.0, 0.0)

#    	glutWireCube(1)
	#wireCube()
 	glColor3f(0.5, 0.0, 1.0)
##	glutWireDodecahedron(2)
	#colorcube()
    	glBegin(GL_LINE_STRIP)
 	glColor3f(0.1, 0.2, 0.3)
	vertices=planecircle(2,8)
	for i in range(len(vertices)):
    		glVertex3fv(vertices[i]);
    	glEnd()

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
