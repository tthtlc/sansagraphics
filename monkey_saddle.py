
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range of parameters u and v
u = np.linspace(-2, 2, 200)
v = np.linspace(-2, 2, 200)
u, v = np.meshgrid(u, v)

# Parametric equation for the Monkey Saddle surface
z = u**3 - 3 * u * v**2

# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(u, v, z, cmap='viridis')

# Set labels and title
ax.set_title('Monkey Saddle Surface')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

