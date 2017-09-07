
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
##  http://mathworld.wolfram.com/Epicycloid.html
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
angle_offset=0.0

def chasing_ngon(radius, ngon,xoffset,yoffset):
	i=0

	#myangle+=angle_step+1/360*2*math.pi+theta
	myangle = 0.0
	angle_step=2*math.pi/ngon
	a = yoffset
	b = xoffset
	niteration=10*ngon

	prevy = a + radius*math.sin(myangle)
    	prevx = b + radius*math.cos(myangle)
	for i in range(1, niteration+1): 
	    	y = a + radius*math.sin(myangle)
	    	x = b + radius*math.cos(myangle)
        	pygame.draw.line(screen,[0,0,255],[prevx,prevy],[x,y],2)
		#if (i%ngon==0):
		#	myangle += 2*math.pi/36
		myangle+=angle_step
		prevx=x
		prevy=y

def my_ngon(R, r, ngon, angle_offset, xoffset, yoffset):

    global PI
    delta = 2*PI/ngon
    prevx = R*math.sin((angle_offset))+r*math.sin((angle_offset)) + xoffset
    prevy = R*math.cos((angle_offset))+r*math.cos((angle_offset)) + yoffset

    for n in range(1,ngon+1):
        ##pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
        theta = n * delta
	y_offset = R*math.cos((theta+angle_offset))+r*math.cos((theta+angle_offset)) + yoffset
	x_offset = R*math.sin((theta+angle_offset))+r*math.sin((theta+angle_offset)) + xoffset
	# print(y_offset, x_offset)
        #cx=int(120*(math.sin((theta)/10)+1)+10)
	#cy=int(120*(math.sin((theta)*6/10)+1)+10)
        #cz=int(120*(math.sin((theta)/10-PI)+1)+10)

        pygame.draw.line(screen,[0,0,255],[prevx,prevy],[x_offset,y_offset],2)
	prevx=x_offset
	prevy=y_offset

screen.fill(white)

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
 
    ## my_ngon(R, r, ngon, angle_offset, xoffset, yoffset):
    ### my_ngon(200, -100, 5, angle_offset, 400, 240)
    chasing_ngon(200, 3,200.0,200.0)
    angle_offset+=2*PI/6/10

    ##pygame.draw.ellipse(screen,black,[y_offset,x_offset,30,30],1/3) 
     
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    ##delta += ddelta
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
