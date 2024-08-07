import pygame
import math

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Triangle Outline")

# Define the square vertices
square_vertices = [(-50, 50), (50, 50), (50, -50), (-50, -50)]

# Function to rotate points around the center
def rotate_point(myfactor, point, angle):
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    x, y = point
    x = x * myfactor
    y = y * myfactor
    return x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta

# Main loop
running = True
angle = 0
clock = pygame.time.Clock()
myfactor = 1.0
rotated_vertices = [rotate_point(myfactor, v, 0) for v in square_vertices]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill((0, 0, 0))

    # Rotate the square

    # Translate to the center of the screen
    translated_vertices = [(x + width // 2, y + height // 2) for x, y in rotated_vertices]
    rotated_vertices = [rotate_point(myfactor, v, angle) for v in square_vertices]
    myfactor += 0.05
    if myfactor > 5:
        myfactor = 1.0
        window.fill((0, 0, 0))
        angle += 0.3

    # Draw the square outline
    pygame.draw.lines(window, (255, 255, 255), True, translated_vertices, 2)

    # Update the display
    pygame.display.flip()

    # Update the angle for the next frame

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()

