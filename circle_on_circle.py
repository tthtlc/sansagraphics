
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
 
# Set the height and width of the screen
size = [800,880]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sansagraphics World")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
R=50
r=10
 
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
    prevx=400.0
    prevy=130.0
 
    # Draw on the screen several green lines from (0,10) to (100,110) 
    # 5 pixels wide using a loop
    totalr=120
    totalR=int(R/r*totalr)
    delta=2*math.pi/totalr
    for n in range(totalR):
        ##pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
	theta = n*delta
	x = (R-r)*math.cos(R*theta/r) + r*math.cos(theta) + prevx
	y = (R-r)*math.sin(R*theta/r) + r*math.sin(theta) + prevy
	if (n>0):
        	pygame.draw.line(screen,red,[prevx,prevy],[x,y],5)
	prevx=x
	prevy=y
    	##pygame.draw.ellipse(screen,black,[y_offset,x_offset,30,30],1/3) 
     
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
