
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
radius=100.0

def figure_of_eight(n, centerx, centery, a, b):
    phi = 2*PI/n
    xorigin=999.9
    cx=0.5
    cy=0.5
    cz=0.5

    for i in range(0, n+1):

	angle = i*phi
	x_offset = radius*(math.cos(a*angle))+centerx
	y_offset = radius*(math.sin(b*angle))+centery
	if (i>0) and (xorigin!=999.9):
		cx=int(120*(math.sin(2*(angle))+1)+10)
		cy=int(120*(math.sin(angle)+1)+10)
		cz=int(120*(math.sin(angle-PI)+1)+10)
       	 	pygame.draw.line(screen,[cx,cy,cz],[xorigin,yorigin],[x_offset,y_offset],2)

	xorigin = x_offset
	yorigin = y_offset

a=2
b=1
n=100
while done == False:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # Clear the screen and set the screen background
    #screen.fill(white)
 
    print "a=%d b=%d n=%d"%(a,b,n)
    figure_of_eight(n, centerx, centery, a, b)

    if (a%2):
    	a = a + 1 
    elif (b%2):
    	b = b + 1 
    elif (a>b):
    	b = b + 1 
    else:
    	a = a + 1 
    n = n + 10
    pygame.display.flip()
    print "Press enter.."
    raw = raw_input()
    screen.fill(black)
 
# Be IDLE friendly
pygame.quit()
