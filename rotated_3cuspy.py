
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
# Import a library of functions called 'pygame'
import pygame
import math
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]

PI = 3.141592653
 
# Set the height and width of the screen
size = [800,480]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sansagraphics World")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
total_rot=100
theta=2.0*PI/total_rot
a=30.0
b=10.0
### a/b=3....three cusp
phi=0.0
shifted_angle=0.0

while done == False:
 
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    #screen.fill(black)
 
    xorigin1 = ((a-b)*math.cos(phi)+b*math.cos((a-b)*phi/b))
    yorigin1 = ((a-b)*math.sin(phi)-b*math.sin((a-b)*phi/b))
    xorigin = xorigin1 * math.cos(shifted_angle) - yorigin1*math.sin(shifted_angle)
    yorigin = xorigin1 * math.sin(shifted_angle) + yorigin1*math.cos(shifted_angle)
    for n in range(total_rot):
        phi += theta
        xoffset1 = ((a-b)*math.cos(phi)+b*math.cos((a-b)*phi/b))
        yoffset1 = ((a-b)*math.sin(phi)-b*math.sin((a-b)*phi/b))
        xoffset = xoffset1 * math.cos(shifted_angle) - yoffset1*math.sin(shifted_angle)
        yoffset = xoffset1 * math.sin(shifted_angle) + yoffset1*math.cos(shifted_angle)

        pygame.draw.line(screen,green,[xorigin+400.0,yorigin+240.0],[xoffset+400.0,yoffset+240.0],2)
        xorigin = xoffset
        yorigin = yoffset
	
    	##pygame.draw.ellipse(screen,black,[y_offset,x_offset,30,30],1/3) 
     
    pygame.display.update()
    phi += 3*theta
    shifted_angle += theta*3
    #pygame.display.flip()
    print "Press enter.."
    raw_input()
    #screen.fill(black)
    #a += 20.0
    b += 10.0
    a = 3*b
 
# Be IDLE friendly
pygame.quit()
