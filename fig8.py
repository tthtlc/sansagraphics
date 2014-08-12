
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

def fig8(n, centerx, centery, a):
    phi = 2*PI/n/a
    xorigin=999.9
    cx=0.5
    cy=0.5
    cz=0.5
    angle=0.0

    for i in range(0, n*a):

	angle += phi
	x_offset = radius*(math.cos(angle)*math.cos(a*angle))+centerx
	y_offset = radius*(math.sin(angle)*math.cos(a*angle))+centery
	if (i==0):
		xorigin1=x_offset
		yorigin1=y_offset
	else:
		cx=int(120*(math.sin(2*(angle))+1)+10)
		cy=int(120*(math.sin(angle)+1)+10)
		cz=int(120*(math.sin(angle-PI)+1)+10)
       		pygame.draw.line(screen,[cx,cy,cz],[xorigin,yorigin],[x_offset,y_offset],2)

	xorigin = x_offset
	yorigin = y_offset
    pygame.draw.line(screen,[cx,cy,cz],[xorigin,yorigin],[xorigin1,yorigin1],2)

a=1
n=50
while done == False:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # Clear the screen and set the screen background
    #screen.fill(white)
 
    print "a=%d n=%d"%(a,n)
    fig8(n, centerx, centery, a)
    a = a+1

    pygame.display.flip()
    print "Press enter.."
    raw = raw_input()
    screen.fill(black)
 
# Be IDLE friendly
pygame.quit()
