
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range of parameters u and v
u = np.linspace(0, 2 * np.pi, 200)
v = np.linspace(-2, 2, 200)
u, v = np.meshgrid(u, v)

# Constants for the surface
a = 1.3  # You can adjust this constant to modify the surface

# Parametric equations for the Capareda surface
x = a * np.cos(u) * np.cosh(v)
y = a * np.sin(u) * np.cosh(v)
z = v + a * np.sin(u) * np.sinh(v)

# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels and title
ax.set_title('Capareda Curves Surface')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

