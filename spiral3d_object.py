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
cx=0.0
cy=0.0

class Simulation:
    def __init__(self, win_width = 640, win_height = 480):
	global cx, cy
	myradius = 50.0

        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("generating spokes in a plane")
        
        self.clock = pygame.time.Clock()

	spoke_number=90
	angle=2*math.pi/spoke_number
        self.vertices=[]
	ngon=5
	
	### generate the first generation of points
	for i in range(spoke_number*ngon):
		x = myradius*(math.cos(ngon*i*angle)+1)*math.cos(i*angle)
		y = myradius*(math.cos(ngon*i*angle)+1)*math.sin(i*angle)
		z = 0.0
		if (i==spoke_number*ngon):
			cx=x
			cy=y
        	self.vertices.append([x,y,z])

        # Define colors for each face
        self.colors = [(255,0,255)]

    def translate(self, v, x, y, z):
	[oldx, oldy, oldz]=v
	newx = oldx + x
	newy = oldy + y
	newz = oldz + z
	return [newx, newy, newz];
    def rotate(self, v, xangle, yangle, zangle):
        """ Rotates the point around the X axis by the given angle in degrees. """
	[oldx, oldy, oldz]=v
        rad = xangle #* math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = oldy * cosa - oldz * sina
        z = oldy * sina + oldz * cosa
	oldy=y
	oldz=z
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = yangle ### * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = - oldz * sina + oldx * cosa
        z = oldz * cosa + oldx * sina
	oldz=z
	oldx=x
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = zangle ## * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = oldx * cosa - oldy * sina
        y = oldx * sina + oldy * cosa
	oldx=x
	oldy=y
	return [oldx, oldy, oldz];
	
    def run(self):
        """ Main Loop """
	global cx, cy
	colour_counter = 0
	count=0

	small_y = 1
	initx = 400
	inity = 200
	yrot = 0.0
	zrot = 0.
	xrot = 0.0
	scene = 1
	angle_quantum = math.pi / 16
	radius=100.0

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(50)
            self.screen.fill((0,32,0))

	    if (scene==1):
	            vlist = []
		    count = count + 1
		    dx = initx + radius * math.cos(yrot/36)
		    dy = inity + radius * math.sin(yrot/36)
	            [new_cx, new_cy, new_cz] = self.translate([cx,cy,0.0], dx, dy, 0.0)
	            for v in self.vertices:
	                w = self.rotate(v, 0, yrot, yrot/36)  
	                r = self.translate(w, dx, dy, 0.0)
			[x,y,z]=r
			vlist.append([x, y])
	
	            for vx,vy in vlist:
			pygame.draw.line(self.screen,mycolor[colour_counter],[new_cx,new_cy],[vx,vy],5)
			colour_counter = colour_counter + 1
			colour_counter = colour_counter % 6
	
		    yrot += angle_quantum
	    
            pygame.display.flip()

if __name__ == "__main__":
    Simulation().run()
