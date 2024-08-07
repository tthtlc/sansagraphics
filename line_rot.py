
import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Line on a Rotating Lemniscate")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Line properties
line_length = 100  # Length of the line
rotation_speed = 0.05  # Speed of rotation of the line itself
lemniscate_speed = 0.01  # Speed of lemniscate rotation
orbit_radius = 100  # Radius of each loop of the lemniscate
orbit_center = (WIDTH // 2, HEIGHT // 2)  # Center of the screen

# Clock for controlling frame rate
clock = pygame.time.Clock()

def get_rotated_line(center, length, angle):
    """Calculate the endpoints of a line given a center, length, and rotation angle."""
    half_length = length / 8
    # Calculate the offsets from the center
    dx = half_length * math.cos(math.radians(angle))
    dy = half_length * math.sin(math.radians(angle))
    # Calculate the endpoints
    start_point = (center[0] - dx, center[1] - dy)
    end_point = (center[0] + dx, center[1] + dy)
    return start_point, end_point

# Main loop
angle = 0  # Starting angle for rotation
lemniscate_angle = 0  # Starting angle for lemniscate rotation
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate the new center of the line (lemniscate motion)
    t = angle  # Use angle as the parameter t in the parametric equation
    x = orbit_radius * math.sin(t) * math.cos(t)
    y = orbit_radius * math.sin(t)
    
    # Rotate the lemniscate
    lemniscate_angle += lemniscate_speed
    cos_theta = math.cos(lemniscate_angle)
    sin_theta = math.sin(lemniscate_angle)
    rotated_x = cos_theta * x - sin_theta * y
    rotated_y = sin_theta * x + cos_theta * y
    
    line_center_x = orbit_center[0] + rotated_x
    line_center_y = orbit_center[1] + rotated_y
    line_center = (line_center_x, line_center_y)
    
    # Increment the angle for the next frame
    angle += rotation_speed

    # Get the current endpoints of the line
    start_point, end_point = get_rotated_line(line_center, line_length, math.degrees(angle))
    
    # Drawing
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, start_point, end_point, 2)  # Draw the rotating line
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

