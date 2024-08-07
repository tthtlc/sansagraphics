
import pygame
import math

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Triangle")

# Define the triangle vertices
triangle_vertices = [(0, -50), (50, 50), (-50, 50)]

# Function to rotate points around the center
def rotate_point(point, angle):
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    x, y = point
    return x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta

# Main loop
running = True
angle = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.fill((0, 0, 0))

    # Rotate the triangle
    rotated_vertices = [rotate_point(v, angle) for v in triangle_vertices]

    # Translate to the center of the screen
    translated_vertices = [(x + width // 2, y + height // 2) for x, y in rotated_vertices]

    # Draw the triangle
    pygame.draw.polygon(window, (255, 255, 255), translated_vertices)

    # Update the display
    pygame.display.flip()

    # Update the angle for the next frame
    angle += 0.04

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()

