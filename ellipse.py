
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
r=100
nrange=60
shift=0.0
delta=0.0

### inverse of factor determine the nos of spokes in the flower shapes
factor=0.25


## ddelta determines the changing rate of the colour
ddelta=2*PI/nrange/10

## sshift determines the rotation rate
sshift=ddelta/6
 
# Set the height and width of the screen
size = [800,600]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sansagraphics World")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
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
 
    for n in range(0,nrange):
        ##pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
	theta = n * 2*PI/nrange
	x_offset = r*(1+math.sin((theta-shift)/factor))*math.cos(theta) + 200.0
	y_offset = r*(1+math.sin((theta-shift)/factor))*math.sin(theta) + 400.0

        cx=int(120*(math.sin((theta-delta)/10)+1)+10)
        cy=int(120*(math.sin((theta-delta)*6/10)+1)+10)
        cz=int(120*(math.sin((theta-delta)/10-PI)+1)+10)

	## ex and ey determine the shape of the ellipse and its rate of change
	ex=int(30*(2+math.sin(theta*2)))
	ey=int(30*(2+math.cos(theta*2)))

	## thickness 0==> filled in
    	pygame.draw.ellipse(screen,[cx,cy,cz],[y_offset,x_offset,ex,ey],0) 
	shift+=sshift
	delta+=ddelta
     
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
