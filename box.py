

# Importing the library
import pygame
 
# Initializing Pygame
pygame.init()
 
# Initializing surface
surface = pygame.display.set_mode((400,300))
 
# Initializing Color
color = (255,0,0)
 
# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()

# infinite loop 
while True : 
	
	# iterate over the list of Event objects 
	# that was returned by pygame.event.get() method. 
	for event in pygame.event.get() : 

		# if event object type is QUIT 
		# then quitting the pygame 
		# and program both. 
		if event.type == pygame.QUIT : 

			# deactivates the pygame library 
			pygame.quit() 

			# quit the program. 
			quit() 

		# Draws the surface object to the screen. 
		pygame.display.update() 

