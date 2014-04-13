"""
 Originally from:
 http://www.pygame.org/project-Rotating+3D+Cube-1859-.html
 Simulation of a rotating 3D Cube
 Developed by Leonel Machava <leonelmachava@gmail.com>

 http://codeNtronix.com
"""
import sys, math, pygame
###from math import pi, sin, cos
from operator import itemgetter

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)
 
	###  angle in degrees
    def rotate(self, angle):
        """ Rotates the point around the YZ plane first """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)

    def rotate8(self, angle):
        """ Rotates the point around the figure of 8 shapes """
    	self.rotate(angle)
        rad = angle * math.pi / 180
        cosa = math.cos(2*rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)
 
    def rotate_in_plane(self, angle):
        """ Rotates the point around the figure of 8 shapes """
    	self.rotate(angle)
        rad = angle * math.pi / 180
        cosa = math.cos(2*rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)
 
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
 
    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, self.z)

class Simulation:
    def __init__(self, win_width = 640, win_height = 480):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("generating spokes in a plane")
        
        self.clock = pygame.time.Clock()

	n=6
	angle=2*math.pi/n
        self.vertices=[]
	for i in range(n):
		x = math.cos(i*angle)
		y = math.sin(i*angle)
		z = 0.0
        	self.vertices.append(Point3D(x,y,z))

        # Define the vertices that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        self.faces  = [(0,1,2,3)]

        # Define colors for each face
        self.colors = [(255,0,255)]

        self.angle = 0
        
    def run(self):
        """ Main Loop """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(50)
            self.screen.fill((0,32,0))

            # It will hold transformed vertices.
            t = []
            
            for v in self.vertices:
                r = v.rotate_in_plane(self.angle)
                s = r.rotate8(self.angle)
                # Transform the point from 3D to 2D
                p = s.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                # Put the point in the list of transformed vertices
		t.append((p.x, p.y))

	    #print t
	    start=99
	    pointlist=[]
            for v1,v2 in t:
		if (start==99):
			startp=(v1, v2)
		start=0
                pointlist.append((v1, v2))
		
            pointlist.append(startp)
		##print startp
	    #print pointlist

            pygame.draw.polygon(self.screen,self.colors[0],pointlist)

	    ### increment by one degree
            self.angle += 1
            
            pygame.display.flip()

if __name__ == "__main__":
    Simulation().run()
