"""
This program demonstrate how to draw a plane in 3D, and capturing the mouse action (via pygame) to rotate the plane.
Rotation of plane is done via polar coordinates and cartesian coordinates.
"""
import sys, math, pygame
from operator import itemgetter

### generate x-z plane vector
PI = 3.141592653
mouseDown = False
theta = 0.0
alpha = 0.0

class PlaneCircle3D:
    def __init__(self, radius = 50.0, ngon = 360):
        theta = 2 * math.pi / ngon
	self.vertices=[]
	for i in range(ngon):
		x = radius * math.cos(i*theta)
		z = radius * math.sin(i*theta)
		y = 0.0
        	self.vertices.append(Point3D(x,y,z))

    def get_vertices(self):
	return self.vertices

    def rotate_theta_alpha(self, theta, alpha):
	##for i in range(len(vertices)):
	new_vertices=[]
        for v in self.vertices:
		v.x *= math.sin(theta) * math.cos(alpha)
		v.y *= math.cos(theta)
		v.z *= math.sin(theta) * math.sin(alpha)
        	new_vertices.append(Point3D(v.x,v.y,v.z))
	return new_vertices
		#self.vertices[i].x *= sin(theta) * cos(alpha)
		#self.vertices[i].y *= cos(theta)
		#self.vertices[i].z *= sin(theta) * sin(alpha)

    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
	for i in range(len(vertices)):
		##self.vertices[i].y *= cos(theta)
		##self.vertices[i].z *= sin(theta) * sin(alpha)
        	rad = angle * math.pi / 180
        	cosa = math.cos(rad)
        	sina = math.sin(rad)
        	self.vertices[i].y = self.vertices[i].y * cosa - self.vertices[i].z * sina
        	self.vertices[i].z = self.vertices[i].y * sina + self.vertices[i].z * cosa
 
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
 
    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, self.z)

WIN_WIDTH=640
WIN_HEIGHT=480

class Simulation:
    def __init__(self, win_width = WIN_WIDTH, win_height = WIN_HEIGHT):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Simulation of a rotating plane")
        
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
        #for v in self.vertices:
        #        r = v.rotateZ(120)
	#	t.append(r)

	#self.vertices.append(t)

        # Define the vertices that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        self.faces  = [(0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15)]

        # Define colors for each face
        self.colors = [(255,0,255),(125,125,125),(100,100,100),(111,118,222)]

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
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r = v.rotateX(self.angle).rotateY(self.angle).rotateZ(self.angle)
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
            for tmp in sorted(avg_z,key=itemgetter(1),reverse=True):
                face_index = tmp[0]
                f = self.faces[face_index]
                pointlist = [(t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y),
                             (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y),
                             (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y),
                             (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y)]
                pygame.draw.polygon(self.screen,self.colors[face_index],pointlist)

                
            self.angle += 1
            
            pygame.display.flip()


    def myrun(self):
        """ Main Loop """
	global mouseDown
	global theta, alpha
	LEFT=1
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
	        #elif event.type == KEYDOWN and event.key == K_ESCAPE:
                #    pygame.quit()
                #    sys.exit()
	        #elif event.type == KEYDOWN and event.key == K_p:
	        #    pygame.image.save(self.screen, "rotating_planar_vector.png")
	        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
			x,y = event.pos
			mouseDown = True
                	prevx = x 
                	prevy = y

		elif event.type == pygame.MOUSEMOTION:
		        if (mouseDown):
				x,y=event.pos
               			theta = x - prevx
               			alpha = y - prevy
	        elif event.type == pygame.MOUSEBUTTONUP:
                	mouseDown = False



#	            body = pm.Body(10, 100)
#	            body.position = p
#	            shape = pm.Circle(body, 10, (0,0))
#	            shape.friction = 0.5
#	            shape.collision_type = COLLTYPE_BALL
#	            space.add(body, shape)
#	            balls.append(shape)
#	        elif event.type == MOUSEBUTTONDOWN and event.button == 3: 
#	            if line_point1 is None:
#	                    line_point1 = Vec2d(event.pos[X], flipy(event.pos[Y]))
#	        elif event.type == MOUSEBUTTONUP and event.button == 3: 
#	            if line_point1 is not None:
#	  
#	                    line_point2 = Vec2d(event.pos[X], flipy(event.pos[Y]))
#	                    print line_point1, line_point2
#	                    body = pm.Body()
#	                    shape= pm.Segment(body, line_point1, line_point2, 0.0)
#	                    shape.friction = 0.99
#	                    space.add(shape)
#	                    static_lines.append(shape)
#	                    line_point1 = None
#	  
#	            elif event.type == KEYDOWN and event.key == K_SPACE:    
#	                run_physics = not run_physics
	  
            	self.clock.tick(50)
            	self.screen.fill((0,32,0))

	    	vertices=PlaneCircle3D(radius=200.0, ngon=360).rotate_theta_alpha(theta, alpha)
	    	cx=0
	    	cy=0
	    	cz=0
            	z_angle =  30 * math.pi / 180
	    	for v in vertices:
        		new_x = -v.z * math.cos(z_angle) + v.x + WIN_WIDTH/2
        		new_y = -v.z * math.sin(z_angle) + v.y + WIN_HEIGHT/2
	    		pygame.draw.line(self.screen,[cz,cx,cy],[WIN_WIDTH/2,WIN_HEIGHT/2],[new_x,new_y],2)
            
            	pygame.display.flip()

if __name__ == "__main__":
    Simulation().myrun()
