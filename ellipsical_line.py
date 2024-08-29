
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Number of points
n_points = 60

# Ellipse parameters
a = 2  # Semi-major axis length
b = 1  # Semi-minor axis length

# Generate the points on the ellipse
theta = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
x = a * np.cos(theta)
y = b * np.sin(theta)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off')

# Initialize the plot
points, = ax.plot(x, y, 'o', markersize=5)
lines = []

for _ in range(n_points):
    line, = ax.plot([], [], 'b')
    lines.append(line)

# Animation function
def update(step):
    for i in range(n_points):
        j = (i + step) % n_points
        lines[i].set_data([x[i], x[j]], [y[i], y[j]])
    return lines

# Create animation
anim = FuncAnimation(fig, update, frames=range(1, n_points), interval=200, blit=True)

# Display the animation
plt.show()

