
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
f1=80.0
f1a=1.0
f2a=2.0
f2=40.0

# Set the height and width of the screen
size = [800,480]
xscreensize=400
yscreensize=240
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sansagraphics World")
 
done = False
clock = pygame.time.Clock()
 
xorigin=999.9
yorigin=999.9
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
 
    phi_step = 2*math.pi/ngon
    phi = 0.0

    for n in range(ngon*3):
        phi += phi_step
        x_offset = f1*math.cos(f1a*phi)+f2*math.cos(f2a*phi) + xscreensize
        y_offset = f1*math.sin(f1a*phi)+f2*math.sin(f2a*phi) + yscreensize
    
        if (n>0) and (xorigin!=999.9):
            cx=int(120*math.sin(phi+phi_step*10)+120)
            cy=int(120*math.sin(phi+phi_step*20)+120)
            cz=int(120*math.sin(phi+phi_step*30)+120)
            pygame.draw.line(screen,[cx,cy,cz],[xorigin,yorigin],[x_offset,y_offset],2)
    
        xorigin = x_offset
        yorigin = y_offset
    
    time.sleep(0.25)

    pygame.display.flip()

pygame.quit()
