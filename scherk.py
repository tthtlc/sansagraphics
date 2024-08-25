
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range of parameters u and v
u = np.linspace(-6, 6, 400)
v = np.linspace(-6, 6, 400)
u, v = np.meshgrid(u, v)

# Parametric equations for the Scherk surface
x = u
y = v
z = np.log(np.cos(v) / np.cos(u))

# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels and title
ax.set_title('Scherk Surface')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

