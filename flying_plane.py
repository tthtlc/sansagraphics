"""
 Originally from:
 http://www.pygame.org/project-Rotating+3D+Cube-1859-.html
 Simulation of a rotating 3D Cube
 Developed by Leonel Machava <leonelmachava@gmail.com>

 http://codeNtronix.com
"""

from OpenGL.GL import *
from OpenGL.GLU import *

from math import * # trigonometry

import pygame # just to get a display

import random, sys, math
from operator import itemgetter
import time

total_count = 0

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)
 
    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)
 
    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)
 
    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)

    def translate(self, vector):
        x = self.x + vector.x
        y = self.y + vector.y
        z = self.z + vector.z
        return Point3D(x, y, z)
 
    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, self.z)

class Simulation:
    def __init__(self, win_width = 900, win_height = 800):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height), pygame.DOUBLEBUF)
        pygame.display.set_caption("Simulation of a rotating plane")

    	glClearColor(0.0, 0.0, 0.0, 1.0)
    	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        self.clock = pygame.time.Clock()

        self.vertices = [
            Point3D(-1,1,-1),
            Point3D(1,1,-1),
            Point3D(1,-1,-1),
            Point3D(-1,-1,-1)
        ]

        self.vertices.append(self.vertices[0].rotateX(60))
        self.vertices.append(self.vertices[1].rotateX(60))
        self.vertices.append(self.vertices[2].rotateX(60))
        self.vertices.append(self.vertices[3].rotateX(60))

        self.vertices.append(self.vertices[0].rotateY(120))
        self.vertices.append(self.vertices[1].rotateY(120))
        self.vertices.append(self.vertices[2].rotateY(120))
        self.vertices.append(self.vertices[3].rotateY(120))

        self.vertices.append(self.vertices[0].rotateZ(60).rotateX(30))
        self.vertices.append(self.vertices[1].rotateZ(60).rotateX(30))
        self.vertices.append(self.vertices[2].rotateZ(60).rotateX(30))
        self.vertices.append(self.vertices[3].rotateZ(60).rotateX(30))

        # Define the vertices that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        self.faces  = [(0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15)]

        # Define colors for each face
        self.colors = [(255,0,255),(0,0,255),(255,0,0),(0,255,255)]

        self.angle = 0
        
    def run(self):
        """ Main Loop """
	global total_count

	PI = 3.141592653
	theta = 0.0
	theta1 = PI*2/360
	theta2 = 0.0

	delta = 0.0

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(50)
            self.screen.fill((0,32,0))

            # It will hold transformed vertices.
            t = []
            
            theta2 += theta1

	    big_radius = 2
            vx=big_radius*(math.sin((theta2-delta)*2))
            vy=big_radius*(math.sin((theta2-delta)*2-PI/2))
            vz=big_radius*(math.sin((theta2-delta)*2-PI/4))
            for v in self.vertices:
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r = v.rotateX(self.angle).rotateY(self.angle).rotateZ(self.angle).translate(Point3D(vx,vy,vz))
                # Transform the point from 3D to 2D
                p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                # Put the point in the list of transformed vertices
                t.append(p)

            # Calculate the average Z values of each face.
            avg_z = []
            i = 0
            for f in self.faces:
                z = (t[f[0]].z + t[f[1]].z + t[f[2]].z + t[f[3]].z) / 4.0
                avg_z.append([i,z])
                i = i + 1

            # Draw the faces using the Painter's algorithm:
            # Distant faces are drawn before the closer ones.
	    xx=0
	    yy=0
	    zz=0
            for tmp in sorted(avg_z,key=itemgetter(1),reverse=True):
                face_index = tmp[0]
                f = self.faces[face_index]
                pointlist = [(t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y),
                             (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y),
                             (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y),
                             (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y)]
		##print t[f[3]].x, t[f[3]].y, t[f[0]].x, t[f[0]].y
        	theta += theta1
                cx=int(250*(math.sin((theta-delta)*3)+1)+10) % 255 +1 
                cy=int(250*(math.sin((theta-delta)*3-PI/2)+1)+10) % 255 +1 
                cz=int(250*(math.sin((theta-delta)*2-PI/4)+1)+10) % 255 +1 
		#print "color = %d %d %d"%(cx,cy,cz)

                #pygame.draw.polygon(self.screen,(cx,cy,cz),pointlist)
                pygame.draw.polygon(self.screen,self.colors[face_index],pointlist)
		##self.colors[:] = [(x, y/7) for x, y in a]
		##self.colors[face_index][:] = [((xx + 25 ) % 255, (yy + 25 ) % 255, (zz + 25 ) % 255) for xx,yy,zz in self.colors[face_index]]
		#xx = (self.colors[face_index][0] + xx + 25) % 255
		#yy = (self.colors[face_index][1] + yy + 25) % 255
		#zz = (self.colors[face_index][2] + zz + 25) % 255
		xx = (xx+self.colors[face_index][0] * 2) % 255 +1 
		yy = (yy+self.colors[face_index][1] * 4) % 255 +1 
		zz = (yy+self.colors[face_index][2] * 8) % 255 +1 
		#print "AAA",self.colors[face_index]
		#print self.colors[face_index][0]
		#print self.colors[face_index][1]
		#print self.colors[face_index][2]
		self.colors[face_index] = (xx,yy,zz)
		#print "BBB",self.colors[face_index]
		#total_count += 1
		#if total_count > 20:
                #    	sys.exit()
		#self.colors[face_index][0] = self.colors[face_index][0] % 255
		#self.colors[face_index][1] += 25
		#self.colors[face_index][1] = self.colors[face_index][1] % 255
		#self.colors[face_index][2] += 25
		#self.colors[face_index][2] = self.colors[face_index][2] % 255
#
                
            self.angle += 1
            
            pygame.display.flip()
#	    time.sleep(0.001)

if __name__ == "__main__":
    Simulation().run()
