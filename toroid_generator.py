
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
# Import a library of functions called 'pygame'
import pygame
import math
import time
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = [  0,  0,  0]
white = [255,255,255]
blue =  [  0,  0,255]
green = [  0,255,  0]
red =   [255,  0,  0]

PI = 3.141592653
r=10
R=200
 
# Set the height and width of the screen
xscreen=900
yscreen=480
x_shift=xscreen/2.0
y_shift=yscreen/2.0
size = [xscreen,yscreen]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sansagraphics World")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
colour=red
xorigin=999.9
yorigin=999.9
total_rot=10000

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
    screen.fill(white)
 
    for n in range(total_rot):
	phi = n * 2*PI/120
	x_offset = r*math.cos(phi) + x_shift
	y_offset = r*math.sin(phi) + y_shift

	if (n>0) and (xorigin!=999.9):
		cx=int(120*(math.sin(2*(phi))+1)+10)
		cy=int(120*(math.sin(phi)+1)+10)
		cz=int(120*(math.sin(phi-PI)+1)+10)
        	pygame.draw.circle(screen,[cx,cy,cz],[int(x_offset),int(y_offset)],R,2)
	xorigin = x_offset
	yorigin = y_offset

    	##pygame.draw.ellipse(screen,black,[y_offset,x_offset,30,30],1/3) 
     
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    r = r + 10
    R = R - 10
    if (R < 100):
	done = True
    pygame.display.flip()
    time.sleep(1)
 
# Be IDLE friendly
pygame.quit()
