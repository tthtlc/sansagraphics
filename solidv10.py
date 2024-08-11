#!/usr/bin/env python

from math import pi, sin, cos
import math
import pyglet
from pyglet.gl import *

# Set up the window with multisampling if possible
try:
    config = Config(sample_buffers=1, samples=4, depth_size=16, double_buffer=True)
    window = pyglet.window.Window(resizable=True, config=config)
except pyglet.window.NoSuchConfigException:
    window = pyglet.window.Window(resizable=True)

@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, width / float(height), 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED

def update(dt):
    global rx, ry, rz
    rx += dt * 30
    ry += dt * 80
    rz += dt * 10
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
    glClearColor(1, 1, 1, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    def vec(*args):
        return (GLfloat * len(args))(*args)

    glLightfv(GL_LIGHT0, GL_POSITION, vec(0.5, 0.5, 1, 0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, vec(0.5, 0.5, 1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, vec(1, 1, 1, 1))
    glLightfv(GL_LIGHT1, GL_POSITION, vec(1, 0, 0.5, 0))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, vec(0.5, 0.5, 0.5, 1))
    glLightfv(GL_LIGHT1, GL_SPECULAR, vec(1, 1, 1, 1))

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(0.5, 0, 0.3, 1))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(1, 1, 1, 1))
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)

class Donut(object):
    def __init__(self, uistacks, uislices, fA, fB, fC, batch, group=None):
        vertices = []
        normals = []

        phi = 0.0
        phistep = 2 * math.pi / uistacks
        thetastep = 2 * math.pi / uislices

        for i in range(uistacks):
            theta = 0.0
            for j in range(uislices):
                x = fA * sin(4 * phi) * sin(phi) * cos(theta) * cos(2 * theta)
                y = fB * sin(4 * phi) * sin(phi) * sin(theta) * cos(2 * theta)
                z = fC * sin(4 * phi) * cos(phi)

                nx = fA * sin(4 * phi) * sin(phi) * sin(theta) * cos(2 * theta)
                ny = fB * sin(4 * phi) * sin(phi) * cos(theta) * cos(2 * theta)
                nz = fC * sin(4 * phi) * cos(phi) * sin(phi)

                vertices.extend([x, y, z])
                normals.extend([nx, ny, nz])
                theta += thetastep
            phi += phistep

        indices = []
        for i in range(uistacks - 1):
            for j in range(uislices - 1):
                p = i * uislices + j
                indices.extend([p, p + uislices, p + uislices + 1])
                indices.extend([p, p + uislices + 1, p + 1])

        self.vertex_list = batch.add_indexed(len(vertices) // 3,
                                             GL_TRIANGLES,
                                             group,
                                             indices,
                                             ('v3f/static', vertices),
                                             ('n3f/static', normals))
       
    def delete(self):
        self.vertex_list.delete()

setup()
batch = pyglet.graphics.Batch()
torus = Donut(120, 60, 1, 3, 1, batch=batch)
rx = ry = rz = 0

pyglet.app.run()

