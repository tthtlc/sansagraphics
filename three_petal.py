
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Number of points
n_points = 120

# Generate the points on the two-petal shape
theta = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
r = np.cos(3 * theta)
x = r * np.cos(theta)
y = r * np.sin(theta)

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

