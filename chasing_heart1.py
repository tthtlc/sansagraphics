
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
r=50
R=200
 
# Set the height and width of the screen
size = [800,480]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sansagraphics World")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
colour=red
thickness=0
i=0

cx=10
cy=155
cz=240
delta=0.0

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
    prevy=240.0
 
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
    for n in range(1200):
        ##pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
	theta = n * 2*PI/60
	y_offset = R*math.cos(theta/10)+r*math.cos(theta) ## + 240.0
	x_offset = R*math.sin(theta/10)+r*math.sin(theta) ## + 400.0
	x_offset1 = x_offset * math.cos(delta) - y_offset*math.sin(delta)
	y_offset1 = x_offset * math.sin(delta) + y_offset*math.cos(delta)
	x_offset = x_offset1
	y_offset = y_offset1
	if (n>0):
        	pygame.draw.line(screen,colour,[prevx,prevy],[x_offset,y_offset],thickness)
	gradient_y=(-R*math.sin(theta/10)/10 - r*math.sin(theta))
	gradient_x=(R*math.cos(theta/10)/10 + r*math.cos(theta))
	m=gradient_y/gradient_x
	norm_x=x_offset
	norm_y=y_offset
	norm_x1=norm_x+gradient_x+40
	norm_y1=norm_y+gradient_y+40
	if (n>0):
        	pygame.draw.line(screen,[cx,cy,cz],[norm_x,norm_y],[norm_x1,norm_y1],thickness)
		cx=int(120*(math.sin(theta)+1)+10)
		cy=int(120*(math.sin(theta/10)+1)+10)
		cz=int(120*(math.sin(theta-PI)+1)+10)
	prevx=x_offset
	prevy=y_offset
	
    	##pygame.draw.ellipse(screen,black,[y_offset,x_offset,30,30],1/3) 
     
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    delta += 2*PI/60
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
