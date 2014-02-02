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

def PlaneCircle3D(radius = 50.0, ngon = 360):
    theta = 2 * math.pi / ngon
    vertices=[]
    for i in range(ngon):
        x = radius * math.cos(i*theta)
        z = radius * math.sin(i*theta)
        y = 0.0
        vertices.append([x,y,z])
    return vertices

def rotate_theta_alpha(object, theta, alpha):
    ##for i in range(len(vertices)):
    new_vertices=[]
    for i in range(len(object)):
	(x,y,z)=object[i]
        x *= math.sin(theta) * math.cos(alpha)
        y *= math.cos(theta)
        z *= math.sin(theta) * math.sin(alpha)
        #print x,y,z
        #v.x *= math.sin(theta) * math.cos(alpha)
        #v.y *= math.cos(theta)
        #v.z *= math.sin(theta) * math.sin(alpha)
        new_vertices.append([x,y,z])
    return new_vertices

def rotateX(object, angle):
    """ Rotates the point around the X axis by the given angle in degrees. """
    for i in range(len(object)):
        ##vertices[i].y *= cos(theta)
        ##vertices[i].z *= sin(theta) * sin(alpha)
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        object.vertices[i].y = object.vertices[i].y * cosa - object.vertices[i].z * sina
        object.vertices[i].z = object.vertices[i].y * sina + object.vertices[i].z * cosa

def rotateY(object, angle):
    """ Rotates the point around the Y axis by the given angle in degrees. """
    rad = angle * math.pi / 180
    cosa = math.cos(rad)
    sina = math.sin(rad)
    z = object.z * cosa - object.x * sina
    x = object.z * sina + object.x * cosa
    return (x, object.y, z)

def rotateZ(object, angle):
    """ Rotates the point around the Z axis by the given angle in degrees. """
    rad = angle * math.pi / 180
    cosa = math.cos(rad)
    sina = math.sin(rad)
    x = object.x * cosa - object.y * sina
    y = object.x * sina + object.y * cosa
    return (x, y, object.z)

win_width=640
win_height=480

clock = pygame.time.Clock()
screen = pygame.display.set_mode((win_width, win_height))

def myinit():

    pygame.init()

    pygame.display.set_caption("Simulation of a rotating plane")


    vertices = [
      [-1,1,-1],
      [1,1,-1],
      [1,-1,-1],
      [-1,-1,-1]
    ]

#    vertices.append(rotateX([vertices[0]],60))
#    vertices.append(rotateX([vertices[1]],60))
#    vertices.append(rotateX([vertices[2]],60))
#    vertices.append(rotateX(vertices[3],60))
#
#    vertices.append(rotateY(vertices[0],120))
#    vertices.append(rotateY(vertices[1],120))
#    vertices.append(rotateY(vertices[2],120))
#    vertices.append(rotateY(vertices[3],120))
#
#    vertices.append(rotateX(rotateZ(vertices[0],60),30))
#    vertices.append(rotateX(rotateZ(vertices[1],60),30))
#    vertices.append(rotateX(rotateZ(vertices[2],60),30))
#    vertices.append(rotateX(rotateZ(vertices[3],60),30))
    #for v in vertices:
    #        r = v.rotateZ(120)
    #       t.append(r)

    #vertices.append(t)

    # Define the vertices that compose each of the 6 faces. These numbers are
    # indices to the vertices list defined above.
    faces  = [(0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15)]

    # Define colors for each face
    colors = [(255,0,255),(125,125,125),(100,100,100),(111,118,222)]


def run():
    """ Main Loop """
    while 1:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      clock.tick(10)
      screen.fill((0,32,0))

      # It will hold transformed vertices.
      t = []

      angle = 0
      for v in vertices:
      # Rotate the point around X axis, then around Y axis, and finally around Z axis.
	      v = rotateX(v,angle)
	      v = rotateY(v,angle)
	      v = rotateZ(v,angle)
	      # Transform the point from 3D to 2D
	      p = project(v,screen.get_width(), screen.get_height(), 256, 4)
	      # Put the point in the list of transformed vertices
	      t.append(p)
      
      # Calculate the average Z values of each face.
      avg_z = []
      i = 0
      for f in faces:
	      z = (t[f[0]].z + t[f[1]].z + t[f[2]].z + t[f[3]].z) / 4.0
	      avg_z.append([i,z])
	      i = i + 1
      
      # Draw the faces using the Painter's algorithm:
      # Distant faces are drawn before the closer ones.
      for tmp in sorted(avg_z,key=itemgetter(1),reverse=True):
      	face_index = tmp[0]
      	f = faces[face_index]
      	pointlist = [(t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y), (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y), (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y), (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y)]
        print t[f[3]].x, t[f[3]].y, t[f[0]].x, t[f[0]].y
        pygame.draw.polygon(screen,colors[face_index],pointlist)
      
      
      angle += 1
      
      pygame.display.flip()

def myrun():
    """ Main Loop """
    global mouseDown
    global theta, alpha
    global clock
    global screen

    LEFT=1
    myinit()
    while 1:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        #elif event.type == KEYDOWN and event.key == K_ESCAPE:
        #    pygame.quit()
        #    sys.exit()
        #elif event.type == KEYDOWN and event.key == K_p:
        #    pygame.image.save(screen, "rotating_planar_vector.png")
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

#                   body = pm.Body(10, 100)
#                   body.position = p
#                   shape = pm.Circle(body, 10, (0,0))
#                   shape.friction = 0.5
#                   shape.collision_type = COLLTYPE_BALL
#                   space.add(body, shape)
#                   balls.append(shape)
#               elif event.type == MOUSEBUTTONDOWN and event.button == 3:
#                   if line_point1 is None:
#                           line_point1 = Vec2d(event.pos[X], flipy(event.pos[Y]))
#               elif event.type == MOUSEBUTTONUP and event.button == 3:
#                   if line_point1 is not None:
#
#                           line_point2 = Vec2d(event.pos[X], flipy(event.pos[Y]))
#                           print line_point1, line_point2
#                           body = pm.Body()
#                           shape= pm.Segment(body, line_point1, line_point2, 0.0)
#                           shape.friction = 0.99
#                           space.add(shape)
#                           static_lines.append(shape)
#                           line_point1 = None
#
#                   elif event.type == KEYDOWN and event.key == K_SPACE:
#                       run_physics = not run_physics

        clock.tick(50)
        screen.fill((0,32,0))

        vertices=rotate_theta_alpha(PlaneCircle3D(radius=200.0, ngon=360), theta, alpha)
	theta += 0.005
	alpha += 0.005
        cx=0
        cy=0
        cz=0
        z_angle =  30 * math.pi / 180
        for i in range(len(vertices)):
	    (x,y,z)=vertices[i]
            new_x = -z * math.cos(z_angle) + x + win_width/2
            new_y = -z * math.sin(z_angle) + y + win_height/2
            ##print vertices[i].x, vertices[i].y, vertices[i].z, new_x, new_y
            pygame.draw.line(screen,[cz,cx,cy],[win_width/2,win_height/2],[new_x,new_y],2)

        pygame.display.flip()

if __name__ == "__main__":
  myrun()
