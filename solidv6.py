#!/usr/bin/env python

from math import pi, sin, cos
import pyglet
from pyglet.gl import *

# Initialize the pyglet window
try:
    # Try to create a window with multisampling (antialiasing)
    config = Config(sample_buffers=1, samples=4, 
                    depth_size=16, double_buffer=True)
    window = pyglet.window.Window(resizable=True, config=config)
except pyglet.window.NoSuchConfigException:
    # Fall back to no multisampling for old hardware
    window = pyglet.window.Window(resizable=True)

@window.event
def on_resize(width, height):
    # Override the default on_resize handler to create a 3D projection
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60., width / float(height), .1, 1000.)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

def update(dt):
    global rx, ry, rz
    rx += dt * 1
    ry += dt * 80
    rz += dt * 30
    rx %= 360
    ry %= 360
    rz %= 360
pyglet.clock.schedule(update)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -4)
    glRotatef(rz, 0, 0, 1)
    glRotatef(ry, 0, 1, 0)
    glRotatef(rx, 1, 0, 0)
    batch.draw()

def setup():
    # One-time GL setup
    glClearColor(1, 1, 1, 1)
    glColor3f(0, 1, 0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)

    # Uncomment this line for a wireframe view
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # Simple light setup
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    # Define a simple function to create ctypes arrays of floats:
    def vec(*args):
        return (GLfloat * len(args))(*args)

    glLightfv(GL_LIGHT0, GL_POSITION, vec(.5, .5, 1, 0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, vec(.5, .5, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, vec(1, 1, 1, 1))
    glLightfv(GL_LIGHT1, GL_POSITION, vec(1, 0, .5, 0))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, vec(.5, .5, .5, 1))
    glLightfv(GL_LIGHT1, GL_SPECULAR, vec(1, 1, 1, 1))

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(0.5, 0, 0.3, 1))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(1, 1, 1, 1))
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)

class Donut(object):
    def __init__(self, uistacks, uislices, fA, fB, fC, batch, group=None):
        # Create the vertex and normal arrays
        vertices = []
        normals = []

        phi = 0.0
        phistep = 2 * pi / (uistacks - 1)
        thetastep = 2 * pi / (uislices - 1)

        for i in range(2 * uistacks):
            theta = 0.
            for j in range(2 * uislices):
                x = fA * sin(phi) * cos(theta)
                y = fB * sin(phi) * sin(theta)
                z = fC * cos(phi)

                nx = fA * sin(phi) * sin(theta)
                ny = fB * sin(phi) * cos(theta)
                nz = fC * cos(phi)

                vertices.extend([x, y, z])
                normals.extend([nx, ny, nz])
                theta += thetastep
            phi += phistep

        # Create a list of triangle indices
        indices = []
        for i in range(2 * uistacks - 1):
            for j in range(2 * uislices - 1):
                p = i * 2 * uislices + j
                indices.extend([p, p + 2 * uislices, p + 2 * uislices + 1])
                indices.extend([p, p + 2 * uislices + 1, p + 1])

        self.vertex_list = batch.add_indexed(len(vertices) // 3, 
                                             GL_TRIANGLE_STRIP,
                                             group,
                                             indices,
                                             ('v3f/static', vertices),
                                             ('n3f/static', normals))
       
    def delete(self):
        self.vertex_list.delete()

setup()
batch = pyglet.graphics.Batch()
torus = Donut(60, 60, 1, 3, 1, batch=batch)
rx = ry = rz = 0

pyglet.app.run()

