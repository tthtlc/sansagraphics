
import pygame

# Initialize the pygame library
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Screen dimensions
width, height = 400, 400
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Draw a Square with Lines")

# Define the square's properties
square_size = 100
square_x = (width - square_size) // 2  # Center the square horizontally
square_y = (height - square_size) // 2  # Center the square vertically

# Define the square's vertices
top_left = (square_x, square_y)
top_right = (square_x + square_size, square_y)
bottom_left = (square_x, square_y + square_size)
bottom_right = (square_x + square_size, square_y + square_size)

# Main loop flag
done = False

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    ##screen.fill(white)

    # Draw the square using lines between the vertices
    print(top_left)
    pygame.draw.line(screen, black, top_left, top_right, 2)
    pygame.draw.line(screen, black, top_right, bottom_right, 2)
    pygame.draw.line(screen, black, bottom_right, bottom_left, 2)
    pygame.draw.line(screen, black, bottom_left, top_left, 2)

    top_left = (0.9*top_left[0], 0.9*top_left[1])
    top_right = (0.9*top_right[0], 0.9*top_right[1])
    bottom_left = (0.9*bottom_left[0], 0.9*bottom_left[1])
    bottom_right = (0.9*bottom_right[0], 0.9*bottom_right[1])

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()

