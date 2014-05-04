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

black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]
mycolor=[red, black, white, blue, green, red]

class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)
 
	###  angle in degrees
    def rotate(self, angle):
        """ Rotates the point around the YZ plane first """
        rad = angle # * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
	self.y = y
        z = self.y * sina + self.z * cosa
	self.z = z
        return ### Point3D(self.x, y, z)

    def rotate8(self, angle):
        """ Rotates the point around the figure of 8 shapes """
    	##self.rotate(angle)
        rad = angle # * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa + self.z * sina
	#self.x = x
        z = self.x * sina + self.z * cosa
	#y = self.y
        return Point3D(x, self.y, z)
 
    def rotate_in_plane(self, angle):
        """ Rotates the point around the figure of 8 shapes """
    	#self.rotate(angle)
        rad = angle ## * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
	#self.x = x
        y = self.x * sina + self.y * cosa
	#self.y = y
        return Point3D(x, y, self.z)
 
    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle #* math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)
 
    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle ### * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = - self.z * sina + self.x * cosa
        z = self.z * cosa + self.x * sina
        return Point3D(x, self.y, z)
 
    def translate(self, x,y,z):
	x = x + self.x
	y = y + self.y
	z = z + self.z
        return Point3D(x, y, z)

    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle ## * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)
 
    def Project2D(self, angle=math.pi/3):
        rad = angle # * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x - self.z * cosa
        y = self.x - self.z * sina
        return (x, y)

    def Project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, self.z)

class Simulation:
    def __init__(self, win_width = 640, win_height = 480):
	myradius = 200.0

        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("generating spokes in a plane")
        
        self.clock = pygame.time.Clock()

	spoke_number=90
	angle=2*math.pi/spoke_number
        self.vertices=[]
	
	### initially all points on the x-y planes
	for i in range(spoke_number*2):
		x = myradius*(math.cos(2*i*angle)+1)*math.cos(i*angle)
		y = myradius*(math.cos(2*i*angle)+1)*math.sin(i*angle)
		z = 0.0
        	self.vertices.append(Point3D(x,y,z))

        # Define colors for each face
        self.colors = [(255,0,255)]

    def run(self):
        """ Main Loop """
	colour_counter = 0
	count=0

	cx = 400
	cy = 200

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(50)
            self.screen.fill((0,32,0))

            vlist = []
	    count = count + 1
            for v in self.vertices:
                w = v.translate(cx, cy, 0.0)
		vlist.append((w.x, w.y))

            for vx,vy in vlist:
		pygame.draw.line(self.screen,mycolor[colour_counter],[cx,cy],[vx,vy],5)
		#print vx, vy
		colour_counter = colour_counter + 1
		colour_counter = colour_counter % 6

            pygame.display.flip()

if __name__ == "__main__":
    Simulation().run()
