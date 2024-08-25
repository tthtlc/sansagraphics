
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range of parameters u and v
u = np.linspace(-2 * np.pi, 2 * np.pi, 200)
v = np.linspace(-1, 1, 200)
u, v = np.meshgrid(u, v)

# Define constants
a = 1  # You can adjust this constant to change the scale of the surface

# Parametric equations for the Bour surface
x = u - (u**3)/3 + u*v**2
y = v - (v**3)/3 + v*u**2
z = u**2 - v**2

# Transform to Bour surface
x_bour = x - a * np.sinh(v) * np.sin(u)
y_bour = y - a * np.sinh(v) * np.cos(u)
z_bour = z + a * np.cosh(v) * np.cos(u)

# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x_bour, y_bour, z_bour, cmap='viridis')

# Set labels and title
ax.set_title('Bour Surface')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

