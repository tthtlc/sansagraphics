
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Triangle vertices
triangle_vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2], [0, 0]])

# Circle parameters
circle_radius = 0.05
num_points = 100

# Function to calculate a point on the line segment
def interpolate(p1, p2, t):
    return p1 + t * (p2 - p1)

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

# Animation function
def animate(i):
    # Determine which line segment the circle is on
    line_index = i // 100
    t = (i % 100) / 100.0
    p1 = triangle_vertices[line_index]
    p2 = triangle_vertices[line_index + 1]
    
    # Interpolate circle center position
    center = interpolate(p1, p2, t)
    
    # Update circle position
    circle.set_data(center[0] + circle_x, center[1] + circle_y)
    return circle,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=300, interval=20, blit=True)

plt.title("Circle Moving Along the Lines of a Triangle")
plt.show()

