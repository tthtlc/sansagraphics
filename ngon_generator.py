
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
# Import a library of functions called 'pygame'
import pygame
import math
import prime_list
 
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
xscreen=900
yscreen=480
centerx=xscreen/2.0
centery=yscreen/2.0
size = [xscreen,yscreen]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sansagraphics World")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
xorigin=999.9
yorigin=999.9
total=1
total_rot=10
n=3

def ngon(n, radius, centerx, centery, shifted_angle):
    phi = 2*PI/n
    xorigin=999.9
    for i in range(0, n+1):
	angle = i*phi
	#x_offset = r*math.cos(phi) + x_shift
	#y_offset = r*math.sin(phi) + y_shift
	x_offset = radius*(math.cos(angle-shifted_angle))+centerx
	y_offset = radius*(math.sin(angle-shifted_angle))+centery

	if (n>0) and (xorigin!=999.9):
		cx=int(120*(math.sin(2*(phi))+1)+10)
		cy=int(120*(math.sin(phi)+1)+10)
		cz=int(120*(math.sin(phi-PI)+1)+10)
        	pygame.draw.line(screen,[cx,cy,cz],[xorigin,yorigin],[x_offset,y_offset],2)

	xorigin = x_offset
	yorigin = y_offset

while done == False:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    #screen.fill(white)
    # move the angle from 0 to x
    # draw the point from radius a (which can be 0 or not) to radius b (slowly increasin)
    # the point as a series of contour which spiral...ie spiral of spiral
 
    shifted_angle = 0.0
    phi = 2*PI/n/2
    radius=40
    for i in range(total_rot):
	if (shifted_angle==0.0):
		shifted_angle = phi
	else:
		shifted_angle = 0.0
	ngon(n, radius, centerx, centery, shifted_angle)
	radius = radius / math.cos(phi)

    n = n + 1 
    pygame.display.flip()
    print "Press enter.."
    raw = raw_input()
    screen.fill(black)
 
# Be IDLE friendly
pygame.quit()
