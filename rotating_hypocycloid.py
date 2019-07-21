
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
a=1.0
b=1.0
special_group=[[1.0, 2.0],[2.0,2.0],[3.0,2.0],[1.0,3.0],[1.0,4.0],[1.0,5.0],[2.0,3.0], [2.0,5.0],[2.0,6.0],[2.0,7.0],[2.0,8.0],[3.0,1.0],[3.0,2.0]]
x_factor=80.0
y_factor=80.0
factora=1.0
factorb=1.0
factorc=1.0
factord=1.0

# Set the height and width of the screen
size = [800,480]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sansagraphics World")
 
done = False
clock = pygame.time.Clock()
 
colour=red
thickness=0
i=0
xorigin=999.9
yorigin=999.9
delta=0.0
total_rot=1000
counter=0
counter_max=len(special_group)
spanning_rate=1.0
ngon=30

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
    if thickness > 100:
	thickness=0
    (a,b) = special_group[counter]

    phi_step = 2*math.pi/ngon
    phi = 0.0

    for n in range(total_rot):

	phi += phi_step
	x_offset = x_factor*((a-b)*math.cos(factora*phi-delta)-b*math.cos(factorc*(a-b)/b*phi))+400.0
	y_offset = y_factor*((a-b)*math.sin(factorb*phi-delta)-b*math.sin(factord*(a-b)/b*phi))+240.0

	if (n>0) and (xorigin!=999.9):
		cx=int(120*(math.sin(2*(phi-delta))+1)+10)
		cy=int(120*(math.sin(phi-delta)+1)+10)
		cz=int(120*(math.sin(phi-delta-math.pi)+1)+10)
        	pygame.draw.line(screen,[cx,cy,cz],[xorigin,yorigin],[x_offset,y_offset],2)
		delta=delta+0.01*spanning_rate

	xorigin = x_offset
	yorigin = y_offset
	
    counter += 1
    counter = counter % 13
    time.sleep(0.25)

    pygame.display.flip()

pygame.quit()
