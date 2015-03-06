### ccc = circle on circle on circle
### using 3 circle vector to draw a construction

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
size = [800,400]
screen = pygame.display.set_mode(size)
cx=3
cy=5
cz=2 
 
pygame.display.set_caption("Sansagraphics World")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
r1=100
r2=20
r3=5
 
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
    xoffset=400.0
    yoffset=200.0
 
    # Draw on the screen several green lines from (0,10) to (100,110) 
    # 5 pixels wide using a loop
    totalr3=120
    totalr2=int(r2/r3*totalr3)
    totalr1=int(r1/r2*totalr2)

    delta=2*math.pi/totalr3
    for n in range(totalr1):
        ##pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
	theta = n*delta
	x = (r1-r2)*math.cos(r3*theta/r1) + (r2-r3)*math.cos(r3*theta/r2) + r3*math.cos(theta) + xoffset
	y = (r1-r2)*math.sin(r3*theta/r1) + (r2-r3)*math.sin(r3*theta/r2) + r3*math.sin(theta) + yoffset
	if (n>0):
        	pygame.draw.line(screen,(cx,cy,cz),[prevx,prevy],[x,y],5)
		cx = (cx + 2)%256
		cy = (cy + 3)%256
		cz = (cz + 5)%256
	prevx=x
	prevy=y
    	##pygame.draw.ellipse(screen,black,[y_offset,x_offset,30,30],1/3) 
     
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
