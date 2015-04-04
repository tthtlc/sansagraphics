"""
 Originally from:
 http://www.pygame.org/project-Rotating+3D+Cube-1859-.html
 Simulation of a rotating 3D Cube
 Developed by Leonel Machava <leonelmachava@gmail.com>

 http://codeNtronix.com
"""
import sys, math, pygame
from operator import itemgetter

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)
 
    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        cosa = math.cos(angle)
        sina = math.sin(angle)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)
 
    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        cosa = math.cos(angle)
        sina = math.sin(angle)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)
 
    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        cosa = math.cos(angle)
        sina = math.sin(angle)
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
        pygame.display.set_caption("Simulation of a rotating plane")
        
        self.clock = pygame.time.Clock()

	self.vertices = []

	PI = math.pi
	init_point=Point3D(200,200,0)
	temp = []
	ngon = 24
	angle = 2*PI/ngon
	(tx,ty,tz) = (200,200,200)
	for i in range(0,ngon):
        	self.vertices.append(Point3D(init_point.x + tx, init_point.y + ty, init_point.z + tz))
		init_point = init_point.rotateZ(angle)   ###.rotateY(angle)

        #for v in self.vertices:
        #        r = v.rotateZ(120)
	#	t.append(r)

	#self.vertices.append(t)

        # Define the vertices that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        #self.faces  = [(0,1,2,3,4,5,6,7,8,9,10,11)]

        # Define colors for each face
        #self.colors = [(0,140,255),(125,125,125),(100,100,100),(111,118,222)]

        self.angle = 0
        
    def run(self):
        """ Main Loop """
	mymod = 0
	angle = 0.0
	cx = 0
	cy = 140
	cz = 255
	counter=0
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(50)

            self.screen.fill((0,32,0))

            # It will hold transformed vertices.
            t = []
            
	    angle_quantum = 2*math.pi / 144

            for v in self.vertices:
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r = v.rotateX(angle).rotateY(angle).rotateZ(angle)
                # Transform the point from 3D to 2D
                #p = r.project(self.screen.get_width(), self.screen.get_height(), 10, 100)

                # Put the point in the list of transformed vertices
                t.append((r.x, r.y))

	    mymod = (mymod + 1 )%4	

	    mymod = 0

	    if counter == 0:
	    	cx = (cx + 6) % 256

	    if counter == 1:
	    	cy = (cy + 7) % 256

	    if counter == 2:
	    	cz = (cz + 8) % 256

	    counter = (counter + 1)%3

            pygame.draw.polygon(self.screen,(cx,cy,cz),t,0) ## 0 == filled
	    
            angle += angle_quantum
            
            pygame.display.flip()

if __name__ == "__main__":

    Simulation().run()
