
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Triangle vertices
triangle_vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2], [0, 0]])

# Circle parameters
circle_radius = 0.05
num_points = 30

# Function to calculate a point on the line segment offset by the circle's radius
def interpolate_with_offset(p1, p2, t, radius, outside=True):
    # Calculate the direction vector of the line segment
    direction = p2 - p1
    direction = direction / np.linalg.norm(direction)
    
    # Calculate the normal to the line segment
    normal = np.array([-direction[1], direction[0]])
    
    # If the circle is outside the triangle, reverse the normal direction
    if outside:
        normal = -normal
    
    # Interpolate the position along the line and offset by the circle's radius
    point_on_line = p1 + t * (p2 - p1)
    offset_point = point_on_line + radius * normal
    return offset_point

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)

# Plot the triangle
triangle_line, = ax.plot(triangle_vertices[:, 0], triangle_vertices[:, 1], 'b-')

# Plot the circle (initial position)
circle_points = np.linspace(0, 2 * np.pi, num_points)
circle_x = circle_radius * np.cos(circle_points)
circle_y = circle_radius * np.sin(circle_points)
circle, = ax.plot(circle_x, circle_y, 'r-')

# Plot the path of the circle's center
center_path_x = []
center_path_y = []
center_path, = ax.plot(center_path_x, center_path_y, 'g--')

# Animation function
def animate(i):
    # Determine which line segment the circle is on
    line_index = i // 100
    t = (i % 100) / 100.0
    p1 = triangle_vertices[line_index]
    p2 = triangle_vertices[line_index + 1]
    
    # Interpolate circle center position with offset for outside placement
    center = interpolate_with_offset(p1, p2, t, circle_radius, outside=True)
    
    # Update circle position
    circle.set_data(center[0] + circle_x, center[1] + circle_y)
    
    # Update the path of the center
    center_path_x.append(center[0])
    center_path_y.append(center[1])
    center_path.set_data(center_path_x, center_path_y)
    
    return circle, center_path

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=300, interval=20, blit=True)

plt.title("Circle Outside the Triangle Moving Along its Edges")
plt.show()

