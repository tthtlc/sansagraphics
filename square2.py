
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
pygame.display.set_caption("Draw a Square")

# Define the square's properties
square_size = 100
square_x = (width - square_size) // 2  # Center the square horizontally
square_y = (height - square_size) // 2  # Center the square vertically

# Main loop flag
done = False

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill(white)

    # Draw the square
    pygame.draw.rect(screen, black, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()

