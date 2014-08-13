import sys
import math

def translate(x0, y0, z0, x,y,z):
	x = x0 + x
	y = y0 + y
	z = z0 + z
        return (x, y, z)


def spherical_to_cartesian3d(r,phi,theta):
	x = r*math.sin(phi)*math.cos(theta)
	y = r*math.sin(phi)*math.sin(theta)
	z = r*math.cos(phi)
	return (x,y,z)

def cartesian3d_to_spherical(x,y,z):
	r = math.sqrt(x*x+y*y+z*z)
	phi = math.acos(z/r)
	theta = y/r/math.sin(phi)
	return (r, phi, theta)

def planespiral(radius,ngon,turn,phi,theta,yc):

	glBlendFunc(GL_SRC_ALPHA_SATURATE, GL_ONE)
	glEnable(GL_BLEND)

    	glBegin(GL_LINE_STRIP)
 	#glColor3f(0.1, 0.2, 0.3)
	theta = 2 * math.pi / ngon
	rad1=radius/turn/ngon
	rad=0.0
	y=0.0
	for i in range(ngon*turn):
    		glColor3fv(Colors[i%8])
		x = rad * math.cos(4*i*theta) 
		z = rad * math.sin(i*theta)
		y += yc 
		(x1,y1,z1) = point_rotatex(x,y,z, phi)
		(x2,y2,z2) = point_rotatez(x1,y1,z1, theta)
		
		rad += rad1
    		glVertex3fv((x2,y2,z2))
    	glEnd()
	return 

def planecircle(radius,ngon):
    	glBegin(GL_LINE_STRIP)
 	glColor3f(0.1, 0.2, 0.3)
        theta = 2 * math.pi / ngon
	for i in range(ngon):
		x = radius * math.cos(i*theta)
		z = radius * math.sin(i*theta)
		y = 0.0
    		glVertex3fv((x,y,z))
    	glEnd()
	return

def rotate_phi_theta(r, phi, theta, delta_r, delta_phi, delta_theta):
	r = r+delta_r
	phi = phi+delta_phi
	theta = theta+delta_theta
	new_vertices=[]
        for v in range(len(vertices)):
		(x,y,z) = vertices[v]
		x *= math.sin(theta) * math.cos(alpha)
		y *= math.cos(theta)
		z *= math.sin(theta) * math.sin(alpha)
        	new_vertices.append((x,y,z))
	return new_vertices


def rotate_theta_alpha(vertices, theta, alpha):
	new_vertices=[]
        for v in range(len(vertices)):
		(x,y,z) = vertices[v]
		x *= math.sin(theta) * math.cos(alpha)
		y *= math.cos(theta)
		z *= math.sin(theta) * math.sin(alpha)
        	new_vertices.append((x,y,z))
	return new_vertices

def point_rotatex(x,y,z, angle):
	rad = angle * math.pi / 180
	cosa = math.cos(rad)
	sina = math.sin(rad)
	y1 = y * cosa - z * sina
	z1 = y * sina + z * cosa
	return (x,y1,z1)

def plane_rotatex(vertices, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
	new_vertices=[]
	for i in range(len(vertices)):
		(x,y,z) = vertices[i]
		(x,y,z)=point_rotatex(x,y,z,angle)	
		new_vertices.append((x,y,z))
	return new_vertices

def point_rotatey(x,y,z, angle):
	rad = angle * math.pi / 180
	cosa = math.cos(rad)
	sina = math.sin(rad)
	z1 = z * cosa - x * sina
	x1 = z * sina + x * cosa
	return (x1,y,z1)
 
def plane_rotatey(vertices, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
	new_vertices=[]
	for i in range(len(vertices)):
		(x,y,z) = vertices[i]
		(x,y,z)=point_rotatey(x,y,z,angle)	
		new_vertices.append((x,y,z))
	return new_vertices

def point_rotatez(x,y,z,angle):
	rad = angle * math.pi / 180
	cosa = math.cos(rad)
        sina = math.sin(rad)
        x1 = x * cosa - y * sina
        y1 = x * sina + y * cosa
	return (x1,y1,z)
 
def plane_rotatez(vertices, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
	new_vertices=[]
	for i in range(len(vertices)):
		(x,y,z) = vertices[i]
		(x,y,z)=point_rotatez(x,y,z,angle)	
		new_vertices.append([x,y,z])
	return new_vertices

def face(a,b,c,d):
    '''draw a face defined by four vertex indices'''
    glBegin(GL_QUADS)
    glColor3fv(Colors[a]);    glVertex3fv(Vertices[a])
    glColor3fv(Colors[b]);    glVertex3fv(Vertices[b])
    glColor3fv(Colors[c]);    glVertex3fv(Vertices[c])
    glColor3fv(Colors[d]);    glVertex3fv(Vertices[d])
    glEnd()

def colorcube():
    '''Draws the entire cube, six faces'''
    face(0,3,2,1)
    face(2,3,7,6)
    face(0,4,7,3)
    face(1,2,6,5)
    face(4,5,6,7)
    face(0,1,5,4)

def edge(A, B):
    '''Sends two vertices down the pipeline.  Presumably they form an edge'''
    glVertex3fv(Vertices[A]);
    glVertex3fv(Vertices[B]);

def wireCube():
    glBegin(GL_LINES)
    ## back
    edge(0,1)
    edge(1,2)
    edge(2,3)
    edge(3,0)
    ## front
    edge(4,5)
    edge(5,6)
    edge(6,7)
    edge(7,4)
    ## sides
    edge(0,4)
    edge(1,5)
    edge(2,6)
    edge(3,7)
    glEnd()

