import sys
import random
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Rotation angles
xrot = 0.2
yrot = 0.0

# Mouse interaction variables
xdiff = 0.0
ydiff = 0.0
mouseDown = False

# Randomization and dynamic behavior
turns1 = 30
turns2 = 30
count = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Background color black
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glClearDepth(1.0)

def my2d_surface(radius1, radius2, turns1, turns2):
    glBlendFunc(GL_SRC_ALPHA_SATURATE, GL_ONE)
    glEnable(GL_BLEND)
    
    itheta = 2 * math.pi / turns1
    jtheta = 2 * math.pi / turns2
    
    glColor3f(1.0, 1.0, 1.0)  # Set color to white

    for i in range(turns1):
        glBegin(GL_LINE_STRIP)
        for j in range(turns2):
            x = radius1 * math.cos(j * jtheta)
            y = radius2 * math.sin(i * itheta)
            z = radius1 * math.cos(i * itheta) + radius2 * math.sin(j * jtheta)
            glVertex3f(x, y, z)
        glEnd()
    
    glDisable(GL_BLEND)

def display():
    global xrot, yrot, turns1, turns2, count

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)

    # Randomize turns every 60 frames
    if count > 60:
        count = 0
    turns1 = random.randint(20, 30)
    turns2 = random.randint(20, 30)
    count += 1

    my2d_surface(100.0, 100.0, turns1, turns2)

    glFlush()
    glutSwapBuffers()

def resize(width, height):
    if height == 0:
        height = 1
    aspect = width / height

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glViewport(0, 0, width, height)
    gluPerspective(45.0, aspect, 1.0, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def idle():
    global xrot, yrot, mouseDown
    if not mouseDown:
        xrot += 0.3
        yrot += 0.4
    glutPostRedisplay()

def keyboard(key, x, y):
    if key == b'\x1b':  # Escape key
        sys.exit(0)

def specialKeyboard(key, x, y):
    global fullscreen
    if key == GLUT_KEY_F1:
        fullscreen = not fullscreen

        if fullscreen:
            glutFullScreen()
        else:
            glutReshapeWindow(500, 500)
            glutPositionWindow(50, 50)

def mouse(button, state, x, y):
    global xrot, yrot, xdiff, ydiff, mouseDown
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        mouseDown = True
        xdiff = x - yrot
        ydiff = -y + xrot
    else:
        mouseDown = False

def mouseMotion(x, y):
    global xrot, yrot, xdiff, ydiff, mouseDown
    if mouseDown:
        yrot = x - xdiff
        xrot = y + ydiff
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(500, 500)

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)

    glutCreateWindow("Dynamic 3D Spiral Surface - White Color")

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(specialKeyboard)
    glutMouseFunc(mouse)
    glutMotionFunc(mouseMotion)
    glutReshapeFunc(resize)

    init()

    glutIdleFunc(idle)
    glutMainLoop()

if __name__ == "__main__":
    main()

