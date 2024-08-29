
import matplotlib.pyplot as plt
import numpy as np

# Number of points
n_points = 60

# Generate the points on the circle
theta = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
x = np.cos(theta)
y = np.sin(theta)

# Plot the points
plt.figure(figsize=(8, 8))
plt.plot(x, y, 'o', markersize=5)

# Connect the points
for i in range(n_points):
    j = (i + 9) % n_points  # 9 steps ahead
    plt.plot([x[i], x[j]], [y[i], y[j]], 'b')

# Set equal scaling
plt.gca().set_aspect('equal', adjustable='box')

# Hide axes
plt.axis('off')

# Show the plot
plt.show()

