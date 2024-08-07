
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Lemniscate Pentagon")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pentagon properties
pentagon_radius = 50  # Radius of the pentagon
rotation_speed = 0.05  # Speed of rotation
lemniscate_speed = 0.01  # Speed of lemniscate rotation
orbit_radius = 100  # Radius of each loop of the lemniscate
orbit_center = (WIDTH // 2, HEIGHT // 2)  # Center of the screen

# Clock for controlling frame rate
clock = pygame.time.Clock()

def get_pentagon_vertices(center, radius, angle):
    """Calculate the vertices of a pentagon given a center, size, and rotation angle."""
    vertices = []
    for i in range(5):
        theta = math.radians(angle + i * 72)  # 72 degrees between pentagon vertices
        x = center[0] + radius * math.cos(theta)
        y = center[1] + radius * math.sin(theta)
        vertices.append((x, y))
    return vertices

# Main loop
angle = 0  # Starting angle for rotation
lemniscate_angle = 0  # Starting angle for lemniscate rotation
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate the new center of the pentagon (lemniscate motion)
    t = angle  # Use angle as the parameter t in the parametric equation
    x = orbit_radius * math.sin(t) * math.cos(t)
    y = orbit_radius * math.sin(t)
    
    # Rotate the lemniscate
    lemniscate_angle += lemniscate_speed
    cos_theta = math.cos(lemniscate_angle)
    sin_theta = math.sin(lemniscate_angle)
    rotated_x = cos_theta * x - sin_theta * y
    rotated_y = sin_theta * x + cos_theta * y
    
    pentagon_center_x = orbit_center[0] + rotated_x
    pentagon_center_y = orbit_center[1] + rotated_y
    pentagon_center = (pentagon_center_x, pentagon_center_y)
    
    # Increment the angle for the next frame
    angle += rotation_speed

    # Get the current vertices of the pentagon
    vertices = get_pentagon_vertices(pentagon_center, pentagon_radius, math.degrees(angle))
    
    # Drawing
    screen.fill(BLACK)
    pygame.draw.polygon(screen, WHITE, vertices)
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

