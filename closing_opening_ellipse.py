
# implement a gradual change of colour

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
r=50
R=300
 
# Set the height and width of the screen
size = [800,480]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Professor Craven's Cool Game")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
delta=0.0
colour=red
thickness=0
i=0
xorigin=400
yorigin=240
cx=1
cy=1
cz=1

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
 
    # Draw on the screen several green lines from (0,10) to (100,110) 
    # 5 pixels wide using a loop
    if colour==red:
	colour=blue
    elif colour==blue:
	colour=green
    else:
	colour=red
    thickness+=1 
    if thickness > 10:
	thickness=0 

    for n in range(1400):
        ##pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
	theta = n * 2*PI/120
	width = int(300*(math.cos(theta/10)+1.0)+10)
	height = int(150*(math.sin(theta/10)+1.0)+10)
	if (n>0):
		cx=int(120*(math.sin((theta-delta)/10)+1)+10)
		cy=int(120*(math.sin((theta-delta)*6/10)+1)+10)
		cz=int(120*(math.sin((theta-delta)/10-PI)+1)+10)
    		pygame.draw.ellipse(screen,[cx,cy,cz],[xorigin,yorigin,width, height], 5)

		###ellipse(Surface, color, Rect, width=0) -> Rect
        	#pygame.draw.ellipse(screen,[cx,cy,cz],[xorigin,yorigin,width, height], 5)
	###	circle(Surface, color, pos, radius, width=0) -> Rect
		delta=delta+0.001
	
    	##pygame.draw.ellipse(screen,black,[y_offset,x_offset,30,30],1/3) 
     
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
