#0## originally from dancing_quad_spiral.py

import sys
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

def spherical_to_cartesian3d(r,phi,theta):
	x = r*math.sin(phi)*math.cos(theta)
	y = r*math.sin(phi)*math.sin(theta)
	z = r*math.cos(phi)
	return (x,y,z)

def cartesian3d_to_spherical(x,y,z):
	r = math.sqrt(x*x+y*y+z*z)
	phi = math.acos(z/r)
	theta = y/r/math.sin(phi)
	return (r, phi, theta)

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


def circling_on_sphere(circle_radius, sphere_radius):

    glBlendFunc(GL_SRC_ALPHA_SATURATE, GL_ONE)
    glEnable(GL_BLEND)

    glBegin(GL_LINE_STRIP)

    ngon=60
    theta1=2*math.pi/ngon
    sphere_gon=5
    yrotate1=2*math.pi/sphere_gon/ngon
    theta=0.0
    y_rotate_angle=0.0

    for i in range(0,ngon):

	## phi = wrt y axis (sinusoidal, between 45 deg and 135 deg)
	## theta = wrt x axis, on the zx plane (normal increment)
	#phi1=math.pi*math.sin(ngon*theta)/4
	#phi=math.pi/2 - phi1
	cx=circle_radius*math.sin(theta)
	cy=circle_radius*math.cos(theta)
	cz=sphere_radius
	y_rotate_angle += yrotate1
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
	theta += theta1
    glVertex3f( rx0, ry0, rz0 )
    glVertex3f( rx1, ry1, rz1 )

    glEnd()
    return 

def planespiral(radius,ngon,turn,phi,theta,yc):

	glBlendFunc(GL_SRC_ALPHA_SATURATE, GL_ONE)
	glEnable(GL_BLEND)

    	glBegin(GL_LINE_STRIP)
 	#glColor3f(0.1, 0.2, 0.3)
	theta = 2 * math.pi / ngon
	rad1=radius/turn/ngon
	rad=0.0
	y=0.0
	for i in range(ngon*turn):
    		glColor3fv(Colors[i%8])
		x = rad * math.cos(4*i*theta) 
		z = rad * math.sin(i*theta)
		y += yc 
		(x1,y1,z1) = point_rotatex(x,y,z, phi)
		(x2,y2,z2) = point_rotatez(x1,y1,z1, theta)
		
		rad += rad1
    		glVertex3fv((x2,y2,z2))
    	glEnd()
	return 

def planecircle(radius,ngon):
    	glBegin(GL_LINE_STRIP)
 	glColor3f(0.1, 0.2, 0.3)
        theta = 2 * math.pi / ngon
	for i in range(ngon):
		x = radius * math.cos(i*theta)
		z = radius * math.sin(i*theta)
		y = 0.0
    		glVertex3fv((x,y,z))
    	glEnd()
	return

def rotate_phi_theta(r, phi, theta, delta_r, delta_phi, delta_theta):
	r = r+delta_r
	phi = phi+delta_phi
	theta = theta+delta_theta
	new_vertices=[]
        for v in range(len(vertices)):
		(x,y,z) = vertices[v]
		x *= math.sin(theta) * math.cos(alpha)
		y *= math.cos(theta)
		z *= math.sin(theta) * math.sin(alpha)
        	new_vertices.append((x,y,z))
	return new_vertices


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
    glColor3fv(Colors[a]);    glVertex3fv(Vertices[a])
    glColor3fv(Colors[b]);    glVertex3fv(Vertices[b])
    glColor3fv(Colors[c]);    glVertex3fv(Vertices[c])
    glColor3fv(Colors[d]);    glVertex3fv(Vertices[d])
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

	circling_on_sphere(1.0, 2.0)

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
