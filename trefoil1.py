
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Define the parametric equations for the trefoil knot
def trefoil_knot(u, v):
    x = (2 + np.cos(3 * u)) * np.cos(2 * u) + v * np.cos(u)
    y = (2 + np.cos(3 * u)) * np.sin(2 * u) + v * np.sin(u)
    z = np.sin(3 * u) + v * np.sin(2 * u)
    return x, y, z

# Generate the vertices for the knot
def generate_trefoil_knot(num_u=60, num_v=60):
    vertices = []

    for i in range(num_u):
        u = 2 * np.pi * i / num_u
        for j in range(num_v):
            v = 0.2 * np.pi * j / num_v - 0.1 * np.pi
            vertices.append(trefoil_knot(u, v))
    return vertices, num_u, num_v

vertices, num_u, num_v = generate_trefoil_knot()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 20, 0, 0, 0, 0, 1, 0)

    glBegin(GL_LINES)
    for i in range(num_u):
        for j in range(num_v):
            next_i = (i + 1) % num_u
            next_j = (j + 1) % num_v

            glVertex3fv(vertices[i * num_v + j])
            glVertex3fv(vertices[next_i * num_v + j])

            glVertex3fv(vertices[i * num_v + j])
            glVertex3fv(vertices[i * num_v + next_j])
    glEnd()

    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1, 50)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    if key == b'\x1b':  # ESC key
        sys.exit()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Trefoil Knot")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()

